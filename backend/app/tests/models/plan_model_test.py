import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from app.models import Plan

@pytest.mark.django_db
def test_create_plan_saves_all_fields():
    plan = Plan.objects.create(
        name='Basic',
        description='Basic plan description.'
    )
    assert plan.name == 'Basic'
    assert plan.description == 'Basic plan description.'

@pytest.mark.django_db
def test_missing_name_raises_validation_error():
    plan = Plan(
        name='',
        description='Tiene descripción pero sin nombre.'
    )
    with pytest.raises(ValidationError) as exc:
        plan.full_clean()
    assert 'name' in exc.value.message_dict

@pytest.mark.django_db
def test_missing_description_raises_validation_error():
    plan = Plan(
        name='Premium',
        description=''
    )
    with pytest.raises(ValidationError) as exc:
        plan.full_clean()
    assert 'description' in exc.value.message_dict

@pytest.mark.django_db
def test_unique_name_constraint():
    # Creo el plan inicial
    Plan.objects.create(
        name='Pro',
        description='Plan Pro.'
    )

    # Intento crear otro con el mismo name ➞ IntegrityError
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Plan.objects.create(
                name='Pro',
                description='Plan Pro duplicado.'
            )
