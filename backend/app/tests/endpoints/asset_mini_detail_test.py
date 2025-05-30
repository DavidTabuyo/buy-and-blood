import pytest
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Asset
import pandas as pd
import yfinance as yf

# DummyTicker for mini detail
class DummyTickerMini:
    def __init__(self, symbol):
        self.symbol = symbol
    def history(self, period="1d", interval="1h"):
        return pd.DataFrame({'Close': [90.0, 100.0, 110.0]})

@pytest.fixture(autouse=True)
def patch_yfinance(monkeypatch):
    monkeypatch.setattr(yf, 'Ticker', DummyTickerMini)

@pytest.mark.django_db
def test_asset_mini_detail():
    asset = Asset.objects.create(name='MiniTest', symbol_yf='MINI', symbol_tv='MINI', type='stock')
    client = APIClient()
    response = client.get(f'/api/asset/mini/{asset.id}/')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data['name'] == asset.name
    assert data['type'] == asset.type
    # price should be last = 110.0
    assert pytest.approx(data['price'], rel=1e-3) == 110.0
    # percentage_change: (110-90)/90*100
    assert pytest.approx(data['percentage_change'], rel=1e-3) == pytest.approx((110-90)/90*100)
    assert data['last_values'] == [90.0, 100.0, 110.0]
