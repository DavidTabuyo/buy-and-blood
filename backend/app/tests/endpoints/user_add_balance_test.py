import pytest
from rest_framework import status
from rest_framework.test import APIClient
from decimal import Decimal
from app.models import User, Asset, Holding

@pytest.mark.django_db
def test_add_balance_unauthenticated():
    client = APIClient()
    # Usar PUT en vez de POST
    response = client.put('/api/user/add-balance/100/')
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_add_balance_invalid_amount():
    user = User.objects.create_user(username='u', password='pass')
    client = APIClient()
    client.force_authenticate(user=user)
    # Amount no válido
    response = client.put('/api/user/add-balance/invalid/')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json().get('error') == 'Invalid amount.'

@pytest.mark.django_db
def test_add_balance_asset_not_found():
    user = User.objects.create_user(username='u', password='pass')
    client = APIClient()
    client.force_authenticate(user=user)
    # Suponiendo que no existe Asset con id hardcodeado en la vista
    response = client.put('/api/user/add-balance/50/')
    # Devuelve 404 si falta asset
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert 'Asset with id' in response.json().get('error', '')

@pytest.mark.django_db
def test_add_balance_success():
    # Preparar user y asset id=9
    user = User.objects.create_user(username='u2', password='pass')
    usd_asset = Asset.objects.create(id=9, name='USD', symbol_yf='USD', symbol_tv='USD', type='currency')
    client = APIClient()
    client.force_authenticate(user=user)

    # Primera llamada crea holding
    response1 = client.put('/api/user/add-balance/150.50/')
    assert response1.status_code == status.HTTP_200_OK
    data1 = response1.json()
    assert data1.get('message') == 'Balance updated successfully.'
    # new_amount = 150.50
    assert Decimal(str(data1.get('new_amount'))) == Decimal('150.50')

    # Segunda llamada suma al holding existente
    response2 = client.put('/api/user/add-balance/100.25/')
    assert response2.status_code == status.HTTP_200_OK
    data2 = response2.json()
    assert Decimal(str(data2.get('new_amount'))) == Decimal('250.75')
