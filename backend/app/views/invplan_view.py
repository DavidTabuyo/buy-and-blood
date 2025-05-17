from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from app.models import Plan, PlanAsset
import yfinance as yf

@api_view(['GET'])
def invplan_details(request, id=None):
    if not id:
        id = request.user.plan.id
        
    try:
        plan = Plan.objects.get(id=id)
    except Plan.DoesNotExist:
        return JsonResponse({'error': 'Plan not found'}, status=404)
    
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

    return JsonResponse(response_data)


@api_view(['GET'])
def invplan_list(request):
    ids = list(Plan.objects.values_list('id', flat=True))
    return Response(ids)