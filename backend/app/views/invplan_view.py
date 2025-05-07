from rest_framework.decorators import api_view
from django.http import JsonResponse
from requests import Response
from app.models import Plan, PlanAsset

@api_view(['GET'])
def invplan_details(request, id):
    try:
        plan = Plan.objects.get(id=id)
    except Plan.DoesNotExist:
        return JsonResponse({'error': 'Plan not found'}, status=404)
    
    plan_assets = PlanAsset.objects.filter(plan_id=id)
    
    labels = [plan_asset.asset.name for plan_asset in plan_assets]
    percentages = [float(plan_asset.percentage) for plan_asset in plan_assets]

    response_data = {
        'name': plan.name,
        'description': plan.description,
        'labels': labels,
        'percentages': percentages,
    }

    return JsonResponse(response_data)
@api_view(['GET'])
def invplan_idlist(request):
    ids = Plan.objects.values_list('id', flat=True)

    return JsonResponse(list(ids))