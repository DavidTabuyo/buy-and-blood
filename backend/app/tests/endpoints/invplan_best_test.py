import pytest
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Plan, PlanAsset, Asset
import yfinance as yf
import pandas as pd

# DummyTicker to mock yfinance behavior
class DummyTicker:
    def __init__(self, symbol):
        self.symbol = symbol

    def history(self, period="1y"):
        # Return a DataFrame with two Close prices: one year ago and now
        # Customize performance based on symbol for distinguishing plans
        if self.symbol == 'AAA':
            closes = [100.0, 200.0]  # 100% return
        elif self.symbol == 'BBB':
            closes = [100.0, 150.0]  # 50% return
        else:
            closes = [100.0, 100.0]  # 0% return
        return pd.DataFrame({'Close': closes})

@pytest.fixture(autouse=True)
def patch_yfinance(monkeypatch):
    monkeypatch.setattr(yf, 'Ticker', DummyTicker)

@pytest.mark.django_db
def test_best_no_plans():
    client = APIClient()
    # JsonResponse(None) without safe=False lanza TypeError
    with pytest.raises(TypeError):
        client.get('/api/invplan/best/')

@pytest.mark.django_db
def test_best_single_plan_single_asset():
    # Crear un activo con rendimiento 100%
    asset = Asset.objects.create(symbol_yf='AAA', symbol_tv='AAA', name='Asset AAA')
    plan = Plan.objects.create(name='Plan Solo', description='Un solo activo')
    PlanAsset.objects.create(plan=plan, asset=asset, percentage=100)

    client = APIClient()
    response = client.get('/api/invplan/best/')
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data['name'] == plan.name
    assert data['description'] == plan.description
    assert data['labels'] == ['Asset AAA']
    assert data['percentages'] == [100.0]
    assert pytest.approx(data['planPercentageChange'], rel=1e-3) == 100.0

@pytest.mark.django_db
def test_best_multiple_plans_choose_best():
    # Plan 1: rendimiento 100%
    asset1 = Asset.objects.create(symbol_yf='AAA', symbol_tv='AAA', name='Asset AAA')
    plan1 = Plan.objects.create(name='Plan 100', description='Rendimiento 100%')
    PlanAsset.objects.create(plan=plan1, asset=asset1, percentage=100)

    # Plan 2: rendimiento 50%
    asset2 = Asset.objects.create(symbol_yf='BBB', symbol_tv='BBB', name='Asset BBB')
    plan2 = Plan.objects.create(name='Plan 50', description='Rendimiento 50%')
    PlanAsset.objects.create(plan=plan2, asset=asset2, percentage=100)

    client = APIClient()
    response = client.get('/api/invplan/best/')
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    # Debe seleccionar plan1 con 100%
    assert data['name'] == plan1.name
    assert data['description'] == plan1.description
    assert data['labels'] == ['Asset AAA']
    assert data['percentages'] == [100.0]
    assert pytest.approx(data['planPercentageChange'], rel=1e-3) == 100.0
