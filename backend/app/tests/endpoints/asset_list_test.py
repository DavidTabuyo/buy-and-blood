import pytest
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Asset

@pytest.mark.django_db
def test_asset_list_no_filters():
    # Sin assets en BD
    client = APIClient()
    response = client.get('/api/asset/list/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

@pytest.mark.django_db
def test_asset_list_filter_type_and_search():
    # Crear varios assets de distintos tipos y nombres
    a1 = Asset.objects.create(name='Apple Inc', symbol_yf='AAPL', symbol_tv='AAPL', type='stock')
    a2 = Asset.objects.create(name='Bitcoin', symbol_yf='BTC-USD', symbol_tv='BTCUSD', type='crypto')
    a3 = Asset.objects.create(name='Currency EUR', symbol_yf='EURUSD', symbol_tv='EURUSD', type='currency')
    a4 = Asset.objects.create(name='Alphabet', symbol_yf='GOOGL', symbol_tv='GOOGL', type='stock')

    client = APIClient()
    # Exclude type=currency by default, so only a1,a2,a4
    resp1 = client.get('/api/asset/list/')
    assert resp1.status_code == status.HTTP_200_OK
    assert set(resp1.json()) == {a1.id, a2.id, a4.id}

    # Filtrar por type=stock
    resp2 = client.get('/api/asset/list/?type=stock')
    assert resp2.status_code == status.HTTP_200_OK
    assert set(resp2.json()) == {a1.id, a4.id}

    # Filtrar por search en nombre
    resp3 = client.get('/api/asset/list/?search=Alpha')
    assert resp3.status_code == status.HTTP_200_OK
    assert resp3.json() == [a4.id]

    # Filtrar por ambos parámetros
    resp4 = client.get('/api/asset/list/?type=crypto&search=bit')
    assert resp4.status_code == status.HTTP_200_OK
    assert resp4.json() == [a2.id]
