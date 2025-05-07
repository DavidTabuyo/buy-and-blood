import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
import yfinance as yf
from app.models import Asset, Transaction  
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def asset_detail(request, id):

    asset = Asset.objects.get(id=id)
    asset = yf.Ticker(asset.symbol_yf)  # Assuming 'ticker' is a field in your model


    important_fields = [
        "symbol",
        "shortName",
        "longName",
        "currency",
        "regularMarketPrice",
        "regularMarketPreviousClose",
        "regularMarketChange",
        "regularMarketChangePercent"
    ]
    
    filtered_info = {clave: asset.info.get(clave) for clave in important_fields}

    for k, v in filtered_info.items():
        print(f'{k}: {v}')

    return Response(filtered_info)

@api_view(['GET'])
def asset_list(request):
    # Captura los parámetros de la solicitud GET asignamos el valor None si no encontramos nada por parámetros
    asset_type = request.GET.get('type', None)  
    search = request.GET.get('search', None)

    # Filtrar los activos según los parámetros recibidos
    assets = Asset.objects.exclude(type='currency')

    if asset_type:
        # Filtra por tipo si se pasó el parámetro 'type'
        assets = assets.filter(type=asset_type)  
    
    if search:
        # Filtra por nombre si se pasó el parámetro 'search'
        assets = assets.filter(name__icontains=search)
    
    # Extraer solo los IDs de los activos filtrados
    asset_ids = list(assets.values_list('id', flat=True))
    
    # Devolver los resultados
    return Response(asset_ids)
    
@api_view(['GET'])
def asset_mini_detail(request, id):
    # Get the asset from the database using the provided ID
    asset = Asset.objects.get(id=id)
    
    ticker = yf.Ticker(asset.symbol_yf)
    
    if asset.type == 'stock':
        # Get the historical data for the stock
        hist = ticker.history(period="1d", interval="1h")
    elif asset.type == 'crypto':
        # Get the historical data for the cryptocurrency
        hist = ticker.history(period="2d", interval="1h").tail(24)
    
    start_price = hist['Close'].iloc[0]
    end_price = hist['Close'].iloc[-1]
    percentage_change = (end_price - start_price) / start_price *100
    
    last_values = hist['Close'].tolist()

    # Return the response with the data obtained
    return Response({
        'name': asset.symbol_yf,
        'type': asset.type,
        'price': end_price,
        'percentage_change': percentage_change,
        'last_values': last_values,
    })

@api_view(['GET'])
def transaction_byid(request, id):

    transactions = Transaction.objects.filter(dest_asset_id=id, user_id=request.user.id)

    # Crear una lista con los datos de las transacciones
    transactions_data = []
    for transaction in transactions:
        transaction_data = {
            'date': transaction.datetime,
            'buyPrice': transaction.price,
            'quantity': transaction.amount,
            'total': transaction.price * transaction.amount,
        }
        transactions_data.append(transaction_data)
    
    # Devolver todas las transacciones como respuesta
    return Response(transactions_data)