from django.http import JsonResponse
from requests import Response
from rest_framework.decorators import api_view
from app.models import Asset
import random

@api_view(['GET'])
def asset_list(request):
    # Retrieve all assets from the database
    assets = list(Asset.objects.all())

    # Randomly select between 3 and 6 assets for the plan
    selected_assets = random.sample(assets, k=min(len(assets), random.randint(3, 6)))

    # Extract labels and generate simulated allocation values
    labels = [asset.name for asset in selected_assets]
    raw_values = [random.uniform(10, 100) for _ in selected_assets]

    # Normalize values to percentage (total = 100)
    total = sum(raw_values)
    values = [round((v / total) * 100, 2) for v in raw_values]

    # Generate a random percentage change between -3% and +3%
    percentage_change = round(random.uniform(-3, 3), 2)

    # Generate a description for the plan
    description = (
        "This chart represents the resource distribution among different categories "
        f"for the '{random.choice(['Global Strategy', 'Tech & Crypto', 'Diversified Plan'])}' plan."
    )

    # Construct the response object
    data = {
        'labels': labels,
        'values': values,
        'percentage_change': percentage_change,
        'description': description,
        'name': "RANDOM PLAN"
    }

    return JsonResponse(data)

