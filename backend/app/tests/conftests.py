# app/tests/conftest.py
import os
import pytest
from django.conf import settings
from django.db import connection
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

# 4) Base de datos limpia: matar conexiones activas a test db y aplicar migraciones
@pytest.fixture(scope='session', autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        test_db_name = connection.creation._get_test_db_name()
        with connection.cursor() as cursor:
            # Matar conexiones activas a la base de datos de test para evitar errores
            cursor.execute(f"""
                SELECT pg_terminate_backend(pid)
                FROM pg_stat_activity
                WHERE datname = '{test_db_name}' AND pid <> pg_backend_pid();
            """)
        call_command("migrate", "--noinput")
    return django_db_setup

# 5) Limpieza de base de datos tras todos los tests
@pytest.fixture(scope="session", autouse=True)
def limpiar_db_al_final(django_db_blocker):
    yield  # aquí corren los tests
    with django_db_blocker.unblock():
        call_command("flush", "--no-input")

# 6) Ejemplo de factory con factory_boy
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
