import pytest
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from app.models import Holding, User, Asset

@pytest.mark.django_db
def test_create_holding_saves_all_fields():
    # Preparar usuario y activo
    user = User.objects.create(
        username='holder',
        email='holder@example.com',
        auth_provider='email'
    )
    asset = Asset.objects.create(
        symbol_yf='XYZ',
        symbol_tv='XYZ',
        name='Asset XYZ',
        type='stock'
    )

    holding = Holding.objects.create(
        user=user,
        asset=asset,
        mean_price=Decimal('50.12345678'),
        amount=Decimal('5.00000000')
    )

    assert holding.user == user
    assert holding.asset == asset
    assert holding.mean_price == Decimal('50.12345678')
    assert holding.amount == Decimal('5.00000000')

@pytest.mark.django_db
def test_full_clean_missing_required_fields_raises_validation_error():
    holding = Holding()
    with pytest.raises(ValidationError) as exc:
        holding.full_clean()
    err_fields = exc.value.message_dict.keys()
    assert 'user' in err_fields
    assert 'asset' in err_fields
    assert 'mean_price' in err_fields
    assert 'amount' in err_fields

@pytest.mark.django_db
def test_cascade_delete_user_deletes_holding():
    user = User.objects.create(
        username='to_delete_holder',
        email='delholder@example.com',
        auth_provider='email'
    )
    asset = Asset.objects.create(
        symbol_yf='AAA',
        symbol_tv='AAA',
        name='Asset A',
        type='stock'
    )
    Holding.objects.create(
        user=user,
        asset=asset,
        mean_price=Decimal('10.0'),
        amount=Decimal('2.0')
    )
    # Al borrar el usuario, debería borrarse también el holding
    user.delete()
    assert Holding.objects.count() == 0

@pytest.mark.django_db
def test_cascade_delete_asset_deletes_holding():
    user = User.objects.create(
        username='user_holder',
        email='userholder@example.com',
        auth_provider='email'
    )
    asset = Asset.objects.create(
        symbol_yf='BBB',
        symbol_tv='BBB',
        name='Asset B',
        type='stock'
    )
    Holding.objects.create(
        user=user,
        asset=asset,
        mean_price=Decimal('20.0'),
        amount=Decimal('3.0')
    )
    # Al borrar el asset, debería borrarse también el holding
    asset.delete()
    assert Holding.objects.count() == 0
