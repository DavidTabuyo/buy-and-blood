import pytest
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Asset, Transaction, User

@pytest.mark.django_db
def test_transaction_byid_unauthenticated():
    asset = Asset.objects.create(name='TransAsset', symbol_yf='TRAS', symbol_tv='TRAS', type='stock')
    client = APIClient()
    response = client.get(f'/api/asset/transactions/{asset.id}/')
    # SessionAuthentication without credentials returns 403 Forbidden
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_transaction_byid_filter_user():
    user1 = User.objects.create_user(username='u1', password='pass')
    user2 = User.objects.create_user(username='u2', password='pass')
    # Crear dos assets: uno como destino y otro como origen
    dest_asset = Asset.objects.create(name='TransDest', symbol_yf='TRAS', symbol_tv='TRAS', type='stock')
    src_asset = Asset.objects.create(name='TransSrc', symbol_yf='TRASRC', symbol_tv='TRASRC', type='stock')

    # Crear transacciones para distintos usuarios, especificando src_asset_id
    t1 = Transaction.objects.create(
        user_id=user1.id,
        dest_asset_id=dest_asset.id,
        src_asset_id=src_asset.id,
        price=10.0,
        amount=2,
        datetime='2025-05-01T10:00:00Z'
    )
    Transaction.objects.create(
        user_id=user2.id,
        dest_asset_id=dest_asset.id,
        src_asset_id=src_asset.id,
        price=20.0,
        amount=1,
        datetime='2025-05-02T12:00:00Z'
    )

    client = APIClient()
    client.force_authenticate(user=user1)
    response = client.get(f'/api/asset/transactions/{dest_asset.id}/')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    tx = data[0]
    assert tx['buyPrice'] == 10.0
    assert tx['quantity'] == 2
    assert tx['total'] == 20.0
