import pytest
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.utils import timezone
from app.models import Transaction, User, Asset

@pytest.mark.django_db
def test_create_transaction_saves_all_fields_and_sets_datetime():
    # Preparar usuario y activos
    user = User.objects.create(
        username='trader',
        email='trader@example.com',
        auth_provider='email'
    )
    src = Asset.objects.create(
        symbol_yf='AAA',
        symbol_tv='AAA',
        name='Asset A',
        type='stock'
    )
    dest = Asset.objects.create(
        symbol_yf='BBB',
        symbol_tv='BBB',
        name='Asset B',
        type='stock'
    )

    tx = Transaction.objects.create(
        user=user,
        src_asset=src,
        dest_asset=dest,
        price=Decimal('123.45678901'),
        amount=Decimal('10.00000000')
    )

    assert tx.user == user
    assert tx.src_asset == src
    assert tx.dest_asset == dest
    assert tx.price == Decimal('123.45678901')
    assert tx.amount == Decimal('10.00000000')
    # datetime debe haberse establecido automáticamente
    assert isinstance(tx.datetime, timezone.datetime)

@pytest.mark.django_db
def test_full_clean_missing_required_fields_raises_validation_error():
    tx = Transaction()
    with pytest.raises(ValidationError) as exc:
        tx.full_clean()
    # Debe reportar errores en los campos obligatorios
    err_fields = exc.value.message_dict.keys()
    assert 'user' in err_fields
    assert 'src_asset' in err_fields
    assert 'dest_asset' in err_fields
    assert 'price' in err_fields
    assert 'amount' in err_fields

@pytest.mark.django_db
def test_cascade_delete_user_deletes_transaction():
    user = User.objects.create(
        username='to_delete_user',
        email='del@example.com',
        auth_provider='email'
    )
    src = Asset.objects.create(
        symbol_yf='CCC',
        symbol_tv='CCC',
        name='Asset C',
        type='stock'
    )
    dest = Asset.objects.create(
        symbol_yf='DDD',
        symbol_tv='DDD',
        name='Asset D',
        type='stock'
    )
    tx = Transaction.objects.create(
        user=user,
        src_asset=src,
        dest_asset=dest,
        price=Decimal('1.0'),
        amount=Decimal('1.0')
    )
    # Eliminar el usuario debe eliminar la transacción por CASCADE
    user.delete()
    assert Transaction.objects.count() == 0

@pytest.mark.django_db
def test_cascade_delete_src_asset_deletes_transaction():
    user = User.objects.create(
        username='to_delete_src',
        email='srcdel@example.com',
        auth_provider='email'
    )
    src = Asset.objects.create(
        symbol_yf='EEE',
        symbol_tv='EEE',
        name='Asset E',
        type='stock'
    )
    dest = Asset.objects.create(
        symbol_yf='FFF',
        symbol_tv='FFF',
        name='Asset F',
        type='stock'
    )
    tx = Transaction.objects.create(
        user=user,
        src_asset=src,
        dest_asset=dest,
        price=Decimal('2.0'),
        amount=Decimal('2.0')
    )
    src.delete()
    assert Transaction.objects.count() == 0

@pytest.mark.django_db
def test_cascade_delete_dest_asset_deletes_transaction():
    user = User.objects.create(
        username='to_delete_dest',
        email='destdel@example.com',
        auth_provider='email'
    )
    src = Asset.objects.create(
        symbol_yf='GGG',
        symbol_tv='GGG',
        name='Asset G',
        type='stock'
    )
    dest = Asset.objects.create(
        symbol_yf='HHH',
        symbol_tv='HHH',
        name='Asset H',
        type='stock'
    )
    tx = Transaction.objects.create(
        user=user,
        src_asset=src,
        dest_asset=dest,
        price=Decimal('3.0'),
        amount=Decimal('3.0')
    )
    dest.delete()
    assert Transaction.objects.count() == 0
