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
    #DEVOLVER TIKER EN VEZ DE ID
    asset_ids = list(Asset.objects.values_list('id', flat=True))
    return Response(asset_ids)
    
@api_view(['GET'])
def asset_mini_detail(request, id):
    ...