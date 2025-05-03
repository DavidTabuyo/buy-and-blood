import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
import yfinance as yf
from app.models import Asset  
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
    assets = Asset.objects.all()

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
    print("XZZZZZZ")
    # Get the asset from the database using the provided ID
    asset = Asset.objects.get(id=id)
    
    # Use yfinance to get the asset data
    ticker = yf.Ticker(asset.symbol_yf)  # Assuming 'ticker' is a field in your model
    
    # Get the historical data for the last 24 hours with an hourly interval
    hist = ticker.history(period="1d", interval="1h")
    
    # Calculate the percentage change from the first to the last closing price
    start_price = hist['Close'].iloc[0]
    end_price = hist['Close'].iloc[-1]
    percentage_change = (end_price - start_price) / start_price
    
    # Get the last 5 closing prices (within the last day)
    last_values = hist['Close'][-5:].tolist()  # Last 5 closing prices

    # Return the response with the data obtained
    # return Response({
    #     'name': asset.name,
    #     'type': asset.type,
    #     'price': end_price,
    #     'percentage_change': percentage_change,
    #     'last_values': last_values,
    # })
    base = random.uniform(5, 15)
    last_values = [round(base + random.uniform(-2, 2), 2) for _ in range(7)]

    # El precio actual será el último valor de la serie
    price = round(last_values[-1], 2)

    # Calcular el porcentaje de cambio respecto al primer valor
    percentage_change = round(((price - last_values[0]) / last_values[0]) * 100, 2)

    return Response({
        'name': "BTC",
        'type': "CURRENCY",
        'price': price,
        'percentage_change': percentage_change,
        'last_values': last_values,
        'type': "crypto"
    })