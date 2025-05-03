from django.http import JsonResponse
from requests import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def asset_list(request):

    data = {
        'labels': ["MSCI WORLD","SP500","BTC"],
        'values': [20,50,30],
        'percentage_change': 1.9,
        'description': (
            "Esta gráfica representa la distribución de recursos "
            "entre las distintas categorías. Esta gráfica representa "
            "la distribución de recursos entre las distintas categorías. "
            "Esta gráfica representa la distribución de recursos"
        ),
        'name': "PLAN DEL DÍA"
    }
    return JsonResponse(data)