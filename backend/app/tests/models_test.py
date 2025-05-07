import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from app.models import Asset

@pytest.mark.django_db
def test_create_asset_uses_default_symbol_yf_and_saves_all_fields():
    asset = Asset.objects.create(
        symbol_tv='AAPL',
        name='Apple Inc.',
        type='stock'
    )
    assert asset.symbol_yf == 'QQQ'
    assert asset.symbol_tv == 'AAPL'
    assert asset.name == 'Apple Inc.'
    assert asset.type == 'stock'

@pytest.mark.django_db
def test_invalid_type_choice_raises_validation_error():
    asset = Asset(
        symbol_tv='BTC',
        name='Bitcoin',
        type='invalid_choice'
    )
    with pytest.raises(ValidationError) as exc:
        asset.full_clean()
    assert 'type' in exc.value.message_dict

@pytest.mark.django_db
def test_uniqueness_constraints_on_fields():
    # Creo el asset válido
    Asset.objects.create(
        symbol_yf='TSLA',
        symbol_tv='TSLA',
        name='Tesla, Inc.',
        type='stock'
    )

    # 1) Mismo symbol_tv ➞ fallo en su propio atomic()
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Asset.objects.create(
                symbol_yf='TSLAX',      # distinto
                symbol_tv='TSLA',       # mismo que el primero
                name='Tesla Duplicate',
                type='stock'
            )

    # 2) Mismo name ➞ otro atomic() independiente
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Asset.objects.create(
                symbol_yf='TSLAXX',
                symbol_tv='TSLAXX',
                name='Tesla, Inc.',     # mismo que el primero
                type='stock'
            )
