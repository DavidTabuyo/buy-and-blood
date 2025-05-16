# app/tests/conftest.py
import os
import pytest
from django.conf import settings
from django.db import connections
from django.core.management import call_command
from rest_framework.test import APIClient
from factory import DjangoModelFactory, Faker

# 1) Si necesitas recargar variables de .env (opcional)
from dotenv import load_dotenv
load_dotenv()

# 2) Forzar usar tu .env DATABASE_URL en tests
@pytest.fixture(autouse=True)
def set_env_db_url(monkeypatch):
    url = os.getenv("DATABASE_URL")
    if url:
        monkeypatch.setenv("DATABASE_URL", url)

# 3) APIClient para peticiones REST
@pytest.fixture
def api_client():
    return APIClient()

# 4) Base de datos limpia: apply migrations o crear tablas
@pytest.fixture(scope='session', autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    # Usa migraciones o crea tablas según tu preferencia:
    with django_db_blocker.unblock():
        # migrate --noinput
        call_command("migrate", "--noinput")
    return django_db_setup

# 5) Ejemplo de factory con factory_boy
class UserFactory(DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL  # 'app.User'
    username = Faker('user_name')
    email    = Faker('email')
    is_active = True
    password = Faker('password')

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Asegura que la contraseña esté hasheada."""
        password = kwargs.pop('password')
        user = model_class.objects.create_user(password=password, *args, **kwargs)
        return user

@pytest.fixture
def usuario_factory():
    return UserFactory
