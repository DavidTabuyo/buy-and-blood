import pytest
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from app.models import PlanAsset, Plan, Asset

@pytest.mark.django_db
def test_create_plan_asset_saves_all_fields():
    # Preparar plan y activo
    plan = Plan.objects.create(
        name='Growth',
        description='Growth plan description.'
    )
    asset = Asset.objects.create(
        symbol_yf='GRT',
        symbol_tv='GRT',
        name='Growth Asset',
        type='stock'
    )

    pa = PlanAsset.objects.create(
        plan=plan,
        asset=asset,
        percentage=Decimal('30.00')
    )

    assert pa.plan == plan
    assert pa.asset == asset
    assert pa.percentage == Decimal('30.00')

@pytest.mark.django_db
def test_full_clean_missing_required_fields_raises_validation_error():
    pa = PlanAsset()
    with pytest.raises(ValidationError) as exc:
        pa.full_clean()
    err_fields = exc.value.message_dict.keys()
    assert 'plan' in err_fields
    assert 'asset' in err_fields
    assert 'percentage' in err_fields

@pytest.mark.django_db
def test_unique_together_plan_and_asset_constraint():
    plan = Plan.objects.create(
        name='Income',
        description='Income plan description.'
    )
    asset = Asset.objects.create(
        symbol_yf='INC',
        symbol_tv='INC',
        name='Income Asset',
        type='stock'
    )
    # Primer vinculo válido
    PlanAsset.objects.create(
        plan=plan,
        asset=asset,
        percentage=Decimal('10.00')
    )
    # Intento duplicado ➞ IntegrityError
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            PlanAsset.objects.create(
                plan=plan,
                asset=asset,
                percentage=Decimal('20.00')
            )

@pytest.mark.django_db
def test_cascade_delete_plan_deletes_plan_asset():
    plan = Plan.objects.create(
        name='Balanced',
        description='Balanced plan description.'
    )
    asset = Asset.objects.create(
        symbol_yf='BAL',
        symbol_tv='BAL',
        name='Balanced Asset',
        type='stock'
    )
    PlanAsset.objects.create(
        plan=plan,
        asset=asset,
        percentage=Decimal('50.00')
    )
    # Borrar el plan debe borrar el PlanAsset
    plan.delete()
    assert PlanAsset.objects.count() == 0

@pytest.mark.django_db
def test_cascade_delete_asset_deletes_plan_asset():
    plan = Plan.objects.create(
        name='Defensive',
        description='Defensive plan description.'
    )
    asset = Asset.objects.create(
        symbol_yf='DEF',
        symbol_tv='DEF',
        name='Defensive Asset',
        type='stock'
    )
    PlanAsset.objects.create(
        plan=plan,
        asset=asset,
        percentage=Decimal('40.00')
    )
    # Borrar el asset debe borrar el PlanAsset
    asset.delete()
    assert PlanAsset.objects.count() == 0
