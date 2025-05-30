from django.http import JsonResponse
from requests import Response
from rest_framework.decorators import api_view
from app.models import Plan, PlanAsset
import yfinance as yf


@api_view(['GET'])
def best_plan(request):
    pass