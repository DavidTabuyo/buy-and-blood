from django.http import JsonResponse
from requests import Response
from rest_framework.decorators import api_view
from app.models import Plan, PlanAsset
import yfinance as yf


@api_view(['GET'])
def asset_list(request):
    # Select a random plan
    plan = Plan.objects.order_by('?').first()
    if not plan:
        return Response({'error': 'No plans available'}, status=404)

    # Retrieve all PlanAsset entries for this plan (including their related Asset)
    plan_assets = (
        PlanAsset.objects
        .filter(plan=plan)
        .select_related('asset')
    )

    # Gather ticker symbols and allocation percentages
    symbols = [pa.asset.symbol_yf for pa in plan_assets]
    allocations = [float(pa.percentage) for pa in plan_assets]

    # If the plan has no assets, return an empty structure
    if not symbols:
        return Response({
            'labels': [],
            'values': [],
            'percentage_change': 0.0,
            'description': plan.description,
            'name': plan.name
        })

    # Download closing prices for the last two trading days
    price_data = yf.download(
        tickers=" ".join(symbols),
        period="2d",
        interval="1d",
        group_by='ticker',
        threads=False,
        progress=False
    )

    # Calculate the daily percentage change for each asset
    pct_changes = []
    for pa in plan_assets:
        symbol = pa.asset.symbol_yf
        # When there's only one ticker, price_data isn't grouped by symbol
        history = price_data[symbol] if len(symbols) > 1 else price_data
        try:
            close_yesterday = history['Close'][-2]
            close_today     = history['Close'][-1]
            pct_change      = (close_today - close_yesterday) / close_yesterday * 100
        except Exception:
            pct_change = 0.0
        pct_changes.append(pct_change)

    # Compute the plan’s weighted average percentage change
    total_allocation = sum(allocations)
    if total_allocation > 0:
        weighted_change = sum(a * c for a, c in zip(allocations, pct_changes)) / total_allocation
    else:
        weighted_change = 0.0

    # Build the response payload
    response_data = {
        'labels':            [pa.asset.name for pa in plan_assets],
        'values':            allocations,
        'percentage_change': round(weighted_change, 2),
        'description':       plan.description,
        'name':              plan.name,
    }

    return Response(response_data)

