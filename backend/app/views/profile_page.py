from app.models import Asset, Holding, Plan, PlanAsset, Transaction
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import yfinance as yf

def get_holding(request, asset_id):
    try:
        holding = Holding.objects.get(user=request.user, asset_id=asset_id)
    except Holding.DoesNotExist:
        return None
    
    asset_name = holding.asset.name
    mean_price = float(holding.mean_price)
    amount = float(holding.amount)
    total_value = amount* mean_price
    
    # Obtener el precio actual del activo usando yfinance
    yf_asset = yf.Ticker(holding.asset.symbol_yf)
    try:
        current_price = yf_asset.fast_info['last_price']
    except Exception:
        current_price = mean_price
        
    # Calcular el cambio en valor y porcentaje
    change_value = (current_price - mean_price) * amount
    percentage_change = (change_value / total_value) * 100
    
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
        return Response(holding)
    else:
        return Response({'error': 'Holding not found'}, status=404)
    
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@transaction.atomic  # Esto asegura que todo el bloque se ejecute como una única transacción atómica
def buyandsell_transaction(request, id):
    src_asset_id = 1
    dest_asset_id = id
    
    asset = yf.Ticker(Asset.objects.get(id=id).symbol_yf)
    price = asset.fast_info['last_price']
    
    # Calcular la cantidad de activo destino a comprar
    amount = request.data.get('total_price') / price

    if not all([src_asset_id, dest_asset_id, price, amount]):
        return Response({"error": "Missing required parameters."}, status=400)
    
    try:
        # Verificar si el usuario tiene suficiente cantidad del activo fuente (src_asset_id)
        holding_src = Holding.objects.get(user=request.user, asset_id=src_asset_id)
        holding_dest, created = Holding.objects.get_or_create(user=request.user, asset_id=dest_asset_id)
        
        # Asegurar que el usuario tiene suficientes activos en src_asset_id para la transacción
        if holding_src.amount < request.data.get('total_price'):
            return Response({"error": "Insufficient funds for the transaction."}, status=400)

        # Crear la transacción
        transaction = Transaction.objects.create(
            user=request.user,
            src_asset_id=src_asset_id,
            dest_asset_id=dest_asset_id,
            price=price,
            amount=amount
        )

        # Actualizar las cantidades en la tabla de holdings
        holding_src.amount -= request.data.get('total_price')  # Restar el monto de dinero gastado
        holding_dest.amount += amount  # Aumentar la cantidad del activo comprado

        holding_src.save()
        holding_dest.save()

        return Response({"message": "Transaction created and holdings updated successfully.", "transaction_id": transaction.id}, status=201)
    
    except Holding.DoesNotExist:
        return Response({"error": "Holding not found for user."}, status=404)
    except Exception as e:
        # Si ocurre cualquier otro error, la transacción atómica hará un rollback de todos los cambios
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
