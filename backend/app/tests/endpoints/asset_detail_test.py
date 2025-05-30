import pytest
import pandas as pd
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Asset
import yfinance as yf

# DummyTicker to mock yfinance behavior and .info
class DummyTickerDetail:
    def __init__(self, symbol):
        self.symbol = symbol
        self.info = {
            'symbol': symbol,
            'shortName': f'Short {symbol}',
            'longName': f'Long {symbol}',
            'currency': 'USD',
            'regularMarketPrice': 100.0,
            'regularMarketPreviousClose': 95.0,
            'regularMarketChange': 5.0,
            'regularMarketChangePercent': 5.26,
        }
    def history(self, period="1d", interval="1h"):
        # hourly points: 90,100,110 for testing
        return pd.DataFrame({'Close': [90.0, 100.0, 110.0]})

@pytest.fixture(autouse=True)
def patch_yfinance(monkeypatch):
    monkeypatch.setattr(yf, 'Ticker', DummyTickerDetail)

@pytest.mark.django_db
def test_asset_detail_stock():
    # Preparar asset stock
    stock = Asset.objects.create(name='TestStock', symbol_yf='TST', symbol_tv='TST', type='stock')
    client = APIClient()
    response = client.get(f'/api/asset/{stock.id}/')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    # Campos filtrados
    for key in ['symbol','shortName','longName','currency','regularMarketPrice','regularMarketPreviousClose','regularMarketChange','regularMarketChangePercent']:
        assert key in data
    # Cambio calculado: (110-90)/90*100 = 22.22...
    assert pytest.approx(data['regularMarketChangePercent'], rel=1e-3) == pytest.approx((110-90)/90*100)

@pytest.mark.django_db
def test_asset_detail_crypto():
    crypto = Asset.objects.create(name='TestCrypto', symbol_yf='CRY', symbol_tv='CRY', type='crypto')
    client = APIClient()
    response = client.get(f'/api/asset/{crypto.id}/')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert pytest.approx(data['regularMarketChangePercent'], rel=1e-3) == pytest.approx((110-90)/90*100)
