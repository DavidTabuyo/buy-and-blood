from rest_framework.decorators import api_view
from django.http import JsonResponse
from requests import Response
from app.models import Plan

@api_view(['GET'])
def invplan_details(request, id):
    plan = Plan.objects.get(id=id)

    #print("Dani dice: ", plan.name,"\nDani repite: ", plan.description)

    #Los assets y el porcentaje se saca de la tabla plan_assets

    response_data = {
        'name': plan.name,
        'description': plan.description
    }

    return JsonResponse(response_data)

@api_view(['GET'])
def invplan_idlist(request):
    ids = Plan.objects.values_list('id', flat=True)

    return JsonResponse(list(ids))