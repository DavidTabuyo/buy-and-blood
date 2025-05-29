import pytest
import pandas as pd
from datetime import datetime, timedelta, date
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Plan, Asset, PlanAsset
import yfinance as yf

# DummyTicker for chart endpoint
class DummyTickerChart:
    def __init__(self, symbol):
        self.symbol = symbol

    def history(self, start, end, interval):
        # Return a single-point DataFrame at 'start' date with Close=100.0
        idx = pd.DatetimeIndex([datetime.combine(start, datetime.min.time())])
        return pd.DataFrame({'Close': [100.0]}, index=idx)

@pytest.fixture(autouse=True)
def patch_yfinance(monkeypatch):
    monkeypatch.setattr(yf, 'Ticker', DummyTickerChart)

@pytest.mark.django_db
def test_invplan_chart_plan_not_found():
    client = APIClient()
    response = client.get('/api/invplan/chart/9999/')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get('error') == 'Plan not found'

@pytest.mark.django_db
def test_invplan_chart_no_assets():
    # Plan without assets
    plan = Plan.objects.create(name='Empty', description='No assets')
    client = APIClient()
    response = client.get(f'/api/invplan/chart/{plan.id}/')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    chart = data.get('chartData')
    # Expect 13 points of zero
    assert isinstance(chart, list)
    assert len(chart) == 13
    assert all(point == 0.0 for point in chart)

@pytest.mark.django_db
def test_invplan_chart_single_asset_full_weight():
    # One asset with 100% allocation
    asset = Asset.objects.create(symbol_yf='AAA', symbol_tv='AAA', name='Asset AAA')
    plan = Plan.objects.create(name='Single', description='One asset')
    PlanAsset.objects.create(plan=plan, asset=asset, percentage=100)

    client = APIClient()
    response = client.get(f'/api/invplan/chart/{plan.id}/')
    assert response.status_code == status.HTTP_200_OK
    chart = response.json().get('chartData')
    # All normalized values = 1.0 for each of 13 points
    assert len(chart) == 13
    assert all(point == pytest.approx(1.0) for point in chart)

@pytest.mark.django_db
def test_invplan_chart_multiple_assets_half_weight():
    # Two assets, each 50%
    asset1 = Asset.objects.create(symbol_yf='AAA', symbol_tv='AAA', name='Asset AAA')
    asset2 = Asset.objects.create(symbol_yf='BBB', symbol_tv='BBB', name='Asset BBB')
    plan = Plan.objects.create(name='Double', description='Two assets')
    PlanAsset.objects.create(plan=plan, asset=asset1, percentage=50)
    PlanAsset.objects.create(plan=plan, asset=asset2, percentage=50)

    client = APIClient()
    response = client.get(f'/api/invplan/chart/{plan.id}/')
    assert response.status_code == status.HTTP_200_OK
    chart = response.json().get('chartData')
    # Each asset contributes 1.0*0.5, sum = 1.0 per point
    assert len(chart) == 13
    assert all(point == pytest.approx(1.0) for point in chart)
