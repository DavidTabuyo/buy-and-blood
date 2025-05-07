import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from app.models import Asset

@pytest.mark.django_db
def test_create_asset_uses_default_symbol_yf_and_saves_all_fields():
    # Sólo pasamos symbol_tv, name y type; symbol_yf debe tomar el default 'QQQ'
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
    # full_clean() comprueba choices y otros validators
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
    # Crea un primer Asset con symbol_yf explícito para evitar conflicto por default
    Asset.objects.create(
        symbol_yf='TSLA',
        symbol_tv='TSLA',
        name='Tesla, Inc.',
        type='stock'
    )
    # Intentar crear otro con el mismo symbol_tv debe fallar
    with pytest.raises(IntegrityError):
        Asset.objects.create(
            symbol_yf='TSLAX',       # distinto para aislar symbol_tv
            symbol_tv='TSLA',        # mismo
            name='Tesla Duplicate',
            type='stock'
        )
    # Intentar crear otro con el mismo name debe fallar
    with pytest.raises(IntegrityError):
        Asset.objects.create(
            symbol_yf='TSLAXX',
            symbol_tv='TSLAXX',
            name='Tesla, Inc.',      # mismo
            type='stock'
        )
