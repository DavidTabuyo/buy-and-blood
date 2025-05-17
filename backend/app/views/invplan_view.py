from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from app.models import Plan, PlanAsset
import yfinance as yf

def invplan_details_util(request, id=None):
    if not id:
        id = request.user.plan.id
        
    try:
        plan = Plan.objects.get(id=id)
    except Plan.DoesNotExist:
        return None
    
    plan_assets = PlanAsset.objects.filter(plan=plan)
    
    year_rentability = 0
    for plan_asset in plan_assets:
        # obtener el valor del activo hace un año con yf y el actual
        
        ticker = plan_asset.asset.symbol_yf  # Suponiendo que el modelo Asset tiene un campo 'ticker'
        data = yf.Ticker(ticker)
        hist = data.history(period="1y")
        price_now = float(hist['Close'][-1])
        price_year_ago = float(hist['Close'][0])
        
        # Calcular el rendimiento
        performance = (price_now - price_year_ago) / price_year_ago * 100
        
        year_rentability += performance * (float(plan_asset.percentage) / 100)
        
    labels = [plan_asset.asset.name for plan_asset in plan_assets]
    percentages = [float(plan_asset.percentage) for plan_asset in plan_assets]

    response_data = {
        'name': plan.name,
        'description': plan.description,
        'labels': labels,
        'percentages': percentages,
        'planPercentageChange': year_rentability,
    }

    return response_data

@api_view(['GET'])
def invplan_details(request, id=None):
    response_data = invplan_details_util(request, id)
    if response_data is None:
        return JsonResponse({'error': 'Plan not found'}, status=404)
    return JsonResponse(response_data)

def invplan_list_util():
    return list(Plan.objects.values_list('id', flat=True))
    
@api_view(['GET'])
def invplan_list(request):
    return Response(invplan_list_util())


@api_view(['GET'])
def best_plan(request):
    best_plan = invplan_details_util(request, 0)
    max_rentability = 0
    
    for plan_id in invplan_list_util():
        response_data = invplan_details_util(request, plan_id)
        if response_data is None:
            continue
        
        if response_data['planPercentageChange'] > max_rentability:
            max_rentability = response_data['planPercentageChange']
            best_plan = response_data
            
    return JsonResponse(best_plan)
        