# app/tests/conftest.py
import os
import pytest
import psycopg2
from django.conf import settings
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

# Nuevo fixture para eliminar la base de datos test antes de crearla
@pytest.fixture(scope='session', autouse=True)
def drop_test_db_before_creation():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        return  # No hay DB configurada, saltar

    import urllib.parse as urlparse
    parsed = urlparse.urlparse(database_url)

    conn_params = {
        'host': parsed.hostname or 'localhost',
        'port': parsed.port or 5432,
        'user': parsed.username,
        'password': parsed.password,
        'dbname': 'postgres'  # conexión a la base administrativa
    }

    # Nombre base test, Django suele prefijar con "test_"
    test_db_name = "test_" + (parsed.path[1:] if parsed.path else "db")

    try:
        conn = psycopg2.connect(**conn_params)
        conn.autocommit = True
        cur = conn.cursor()

        # Terminar conexiones activas a la base de test
        cur.execute(f"""
            SELECT pg_terminate_backend(pid)
            FROM pg_stat_activity
            WHERE datname = %s AND pid <> pg_backend_pid();
        """, (test_db_name,))

        # Eliminar la base de datos de test si existe
        cur.execute(f"DROP DATABASE IF EXISTS {test_db_name};")

        cur.close()
        conn.close()
        print(f"Base de datos de test '{test_db_name}' eliminada antes de crearla.")
    except Exception as e:
        print(f"Error eliminando base de datos de test '{test_db_name}': {e}")

# 3) APIClient para peticiones REST
@pytest.fixture
def api_client():
    return APIClient()

# 4) Base de datos limpia: apply migrations o crear tablas
@pytest.fixture(scope='session', autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
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
