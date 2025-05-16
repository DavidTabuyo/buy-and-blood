from app.models import Asset, Holding, Plan, PlanAsset, Transaction
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import yfinance as yf

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def holdings(request):
    holdings = [
        { 'id': 1, 'asset': 'SPDR S&P 500 ETF', 'quantity': 100.234, 'value': 45000.56, 'change_value': 500.12, 'percentage_change': 1.123 },
        { 'id': 2, 'asset': 'Vanguard Total Stock Market ETF', 'quantity': 150.567, 'value': 34500.78, 'change_value': 300.45, 'percentage_change': 0.874 },
        { 'id': 3, 'asset': 'iShares MSCI Emerging Markets ETF', 'quantity': 200.891, 'value': 11000.34, 'change_value': 100.23, 'percentage_change': 0.912 },
        { 'id': 4, 'asset': 'Invesco QQQ Trust', 'quantity': 50.123, 'value': 18500.89, 'change_value': 700.67, 'percentage_change': 3.934 },
        { 'id': 5, 'asset': 'Schwab U.S. Dividend Equity ETF', 'quantity': 120.456, 'value': 9000.12, 'change_value': 150.34, 'percentage_change': 1.693 },
        { 'id': 6, 'asset': 'ARK Innovation ETF', 'quantity': 80.789, 'value': 9600.45, 'change_value': 400.56, 'percentage_change': 4.354 },
        { 'id': 7, 'asset': 'iShares Russell 2000 ETF', 'quantity': 70.234, 'value': 14700.67, 'change_value': 350.78, 'percentage_change': 2.432 },
        { 'id': 8, 'asset': 'Vanguard FTSE Developed Markets ETF', 'quantity': 180.567, 'value': 9000.89, 'change_value': 80.12, 'percentage_change': 0.894 },
        { 'id': 9, 'asset': 'Bitcoin (BTC)', 'quantity': 0.543, 'value': 30000.34, 'change_value': 2000.45, 'percentage_change': 7.143 },
        { 'id': 10, 'asset': 'Ethereum (ETH)', 'quantity': 2.345, 'value': 4000.56, 'change_value': 300.67, 'percentage_change': 8.114 },
    ]

    return Response(holdings)

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
