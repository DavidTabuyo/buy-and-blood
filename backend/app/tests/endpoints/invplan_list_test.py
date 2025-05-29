import pytest
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Plan

@pytest.mark.django_db
def test_invplan_list_empty():
    client = APIClient()
    response = client.get('/api/invplan/list/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

@pytest.mark.django_db
def test_invplan_list_multiple_plans():
    # Crear tres planes
    p1 = Plan.objects.create(name='Plan A', description='Desc A')
    p2 = Plan.objects.create(name='Plan B', description='Desc B')
    p3 = Plan.objects.create(name='Plan C', description='Desc C')

    client = APIClient()
    response = client.get('/api/invplan/list/')
    assert response.status_code == status.HTTP_200_OK
    # Comprobar que devuelve los IDs en el mismo orden de creación
    assert response.json() == [p1.id, p2.id, p3.id]