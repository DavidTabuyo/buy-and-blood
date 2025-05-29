import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from app.models import User

@pytest.mark.django_db
def test_create_user_saves_all_fields_and_default_plan_null():
    user = User.objects.create(
        username='testuser',
        email='test@example.com',
        auth_provider='email'
    )
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.auth_provider == 'email'
    assert user.plan is None

@pytest.mark.django_db
def test_missing_auth_provider_raises_validation_error():
    user = User(
        username='nouserprov',
        email='no@example.com',
        auth_provider=''
    )
    with pytest.raises(ValidationError) as exc:
        user.full_clean()
    assert 'auth_provider' in exc.value.message_dict

@pytest.mark.django_db
def test_username_uniqueness_constraint():
    # Creo el usuario inicial
    User.objects.create(
        username='uniqueuser',
        email='first@example.com',
        auth_provider='email'
    )

    # Intento crear otro con el mismo username ➞ IntegrityError
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            User.objects.create(
                username='uniqueuser',
                email='second@example.com',
                auth_provider='email'
            )

@pytest.mark.django_db
def test_duplicate_email_allowed():
    # Por defecto, email no es único, así que duplicados deben permitirse
    User.objects.create(
        username='user1',
        email='same@example.com',
        auth_provider='email'
    )
    User.objects.create(
        username='user2',
        email='same@example.com',
        auth_provider='google'
    )
    assert User.objects.filter(email='same@example.com').count() == 2
