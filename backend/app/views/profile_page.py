from decimal import Decimal
from app.models import Asset, Holding, Plan, PlanAsset, Transaction
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import yfinance as yf
from django.db.models import F
from decimal import Decimal, InvalidOperation

def get_holding(request, asset_id):
    try:
        holding = Holding.objects.get(user=request.user, asset_id=asset_id)
    except Holding.DoesNotExist:
        return None
    
    asset_name = holding.asset.name
    mean_price = float(holding.mean_price)
    amount = float(holding.amount)
    initial_value = amount* mean_price
    
    # Obtener el precio actual del activo usando yfinance
    yf_asset = yf.Ticker(holding.asset.symbol_yf)
    try:
        current_price = yf_asset.fast_info['last_price']
    except Exception:
        current_price = mean_price
        
    # Calcular el cambio en valor y porcentaje
    change_value = (current_price - mean_price) * amount
    percentage_change = (change_value / initial_value) * 100
    
    total_value = amount * current_price
    
    return {
        'asset_id': asset_id,
        'asset_name': asset_name,
        'mean_price': mean_price,
        'amount': amount,
        'total_value': total_value,
        'current_price': current_price,
        'change_value': change_value,
        'percentage_change': percentage_change,
    }
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def holdings(request):
    holdings = []
    for holding in Holding.objects.filter(user=request.user):
        asset_id = holding.asset_id
        
        holding_info = get_holding(request, asset_id)
        if holding_info:
            holdings.append(holding_info)
        else:
            Response({'error': 'Holding not found'}, status=404)
            
    return Response(holdings)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def holding(request, asset_id): 
    holding = get_holding(request, asset_id)
    if holding:
        print()
        print()
        print()
        print(holding)
        print()
        print()
        return Response(holding)
    else:
        return Response({'error': 'Holding not found'}, status=404)
    
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@transaction.atomic  # Esto asegura que todo el bloque se ejecute como una única transacción atómica
def buyandsell_transaction(request, asset_id):
    src_asset_id = 9
    dest_asset_id = int(asset_id)
    asset = yf.Ticker(Asset.objects.get(id=dest_asset_id).symbol_yf)
    
    # Obtenemos el valor bruto (string o numérico) y lo convertimos a Decimal
    transaction_money_raw = request.data.get('transaction_money')
    try:
        transaction_money = Decimal(str(transaction_money_raw))
    except (InvalidOperation, TypeError):
        return Response({"error": "Valor de 'transaction_money' inválido."}, status=400)
    
    # Obtenemos el precio como float y lo convertimos a Decimal
    try:
        current_dest_price = Decimal(str(asset.fast_info['last_price']))
    except (InvalidOperation, KeyError, TypeError):
        return Response({"error": "No se pudo obtener el precio actual del activo."}, status=400)
    
    try:
        # Verificar si el usuario tiene suficiente cantidad del activo fuente (src_asset_id)
        holding_src = Holding.objects.get(user=request.user, asset_id=src_asset_id)
        holding_dest, _ = Holding.objects.get_or_create(
            user=request.user,
            asset_id=dest_asset_id,
            defaults={
                'mean_price': current_dest_price,
                'amount': Decimal('0')
            }
        )

        # Calculamos el dinero total en cada holding (amount * mean_price), que ya son Decimals
        src_money = holding_src.amount * holding_src.mean_price
        dest_money = holding_dest.amount * holding_dest.mean_price

        # Asegurar que el usuario tiene suficientes fondos para la transacción
        # Aquí se asume que: para vender src_asset, transaction_money no pueda exceder src_money
        # y para comprar dest_asset, transaction_money no pueda hacer que dest_money sea negativo.
        if transaction_money > src_money and transaction_money > -dest_money:
            return Response({"error": "Fondos insuficientes para la transacción."}, status=400)

        # Calculamos la cantidad de unidades a transferir (transaction_money / precio actual).
        # Ambos son Decimal, así que la división es precisa.
        amount_units = transaction_money / current_dest_price

        # Creamos la transacción
        transaction = Transaction.objects.create(
            user=request.user,
            src_asset_id=src_asset_id,
            dest_asset_id=dest_asset_id,
            price=current_dest_price,
            amount=amount_units,
        )

        # Actualizar las cantidades en la tabla de holdings
        # Reducimos el holding origen: restamos las unidades equivalentes a 'transaction_money'
        holding_src.amount = holding_src.amount - (transaction_money / holding_src.mean_price)

        # Calculamos el nuevo dinero total en dest antes de actualizar amount
        new_dest_money = (holding_dest.amount * holding_dest.mean_price) + transaction_money
        # Actualizamos el amount de dest añadiendo las nuevas unidades
        holding_dest.amount = holding_dest.amount + amount_units
        
        # Actualizamos mean_price en dest como: (nuevo dinero total) / (nuevas unidades totales)
        # Siempre verificamos que holding_dest.amount != 0 para evitar división por cero.
        if holding_dest.amount > 0:
            holding_dest.mean_price = new_dest_money / holding_dest.amount
        else:
            holding_dest.mean_price = Decimal('0')

        holding_src.save()
        holding_dest.save()

        return Response(
            {
                "message": "Transacción creada y holdings actualizados correctamente.",
                "transaction_id": transaction.id
            },
            status=201
        )

    except Holding.DoesNotExist:
        return Response({"error": "Holding no encontrado para el usuario."}, status=404)
    except Exception as e:
        # Si ocurre cualquier otro error, la transacción atómica hará rollback
        return Response({"error": str(e)}, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def set_investing_plan(request, id):
    try:
        plan = Plan.objects.get(id=id)
    except Plan.DoesNotExist:
        return Response({'error': 'Plan not found'}, status=404)
    
    
    user = request.user
    
    if user.plan == plan:
        return Response({'error': 'User already has this plan'}, status=400)
    
    user.plan = plan
    user.save()

    return Response({'message': 'Investing plan updated successfully'}, status=200)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@transaction.atomic
def add_balance(request, amount):
    try:
        f_amount = float(amount)
    except (TypeError, ValueError):
        return Response(
            {"error": "Invalid amount."},
            status=400
        )

    user = request.user
    asset_id = 9

    # Asegurarnos de que el asset 9 existe
    try:
        usd_asset = Asset.objects.get(pk=asset_id)
    except Asset.DoesNotExist:
        return Response(
            {"error": f"Asset with id {asset_id} not found."},
            status=404
        )

    # Obtener o crear el holding
    holding, created = Holding.objects.get_or_create(
        user=user,
        asset=usd_asset,
        defaults={
            'mean_price': 1.0,
            'amount': f_amount
        }
    )

    if not created:
        # Si ya existía, sumamos el nuevo saldo
        holding.amount = F('amount') + f_amount
        holding.save()
        # refrescamos el valor real desde la base de datos
        holding.refresh_from_db()

    return Response({
        "message": "Balance updated successfully.",
        "new_amount": holding.amount
    }, status=200)