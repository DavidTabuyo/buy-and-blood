import pytest
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Plan, User

@pytest.mark.django_db
def test_set_plan_unauthenticated():
    client = APIClient()
    response = client.put('/api/user/set-investing-plan/1/')
    # Sin autenticación devuelve 403 Forbidden
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_set_plan_not_found():
    # Crear usuario y autenticar
    user = User.objects.create_user(username='u', password='pass')
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.put('/api/user/set-investing-plan/9999/')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get('error') == 'Plan not found'

@pytest.mark.django_db
def test_set_plan_already_assigned():
    # Crear plan y asignar al usuario
    plan = Plan.objects.create(name='Plan1', description='D')
    user = User.objects.create_user(username='u2', password='pass')
    user.plan = plan
    user.save()

    client = APIClient()
    client.force_authenticate(user=user)
    response = client.put(f'/api/user/set-investing-plan/{plan.id}/')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json().get('error') == 'User already has this plan'

@pytest.mark.django_db
def test_set_plan_success():
    # Crear planes y usuario
    plan_old = Plan.objects.create(name='PlanOld', description='Old')
    plan_new = Plan.objects.create(name='PlanNew', description='New')
    user = User.objects.create_user(username='u3', password='pass')
    user.plan = plan_old
    user.save()

    client = APIClient()
    client.force_authenticate(user=user)
    response = client.put(f'/api/user/set-investing-plan/{plan_new.id}/')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data.get('message') == 'Investing plan updated successfully'

    # Refrescar usuario y comprobar cambio de plan
    user.refresh_from_db()
    assert user.plan_id == plan_new.id
