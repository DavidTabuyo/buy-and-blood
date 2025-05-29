import pytest
from rest_framework import status
from rest_framework.test import APIClient
from app.models import User

@pytest.mark.django_db
def test_logout_unauthenticated():
    client = APIClient()
    response = client.post('/api/user/logout/')
    # Sin autenticación devuelve 403 Forbidden
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_logout_success():
    user = User.objects.create_user(username='u', password='pass')
    client = APIClient()
    client.force_authenticate(user=user)
    # Simular sesión previa
    response = client.post('/api/user/logout/')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data.get('detail') == 'Sesión cerrada correctamente.'
    # GET en logout no está permitido: 405 Method Not Allowed
    response2 = client.get('/api/user/logout/')
    assert response2.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
