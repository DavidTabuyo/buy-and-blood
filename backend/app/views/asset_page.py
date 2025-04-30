from rest_framework.response import Response
from rest_framework.decorators import api_view
import yfinance as yf
from app.models import Asset  


@api_view(['GET'])
def asset_detail(request, ticker):
    asset = yf.Ticker(ticker)

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
    ...