import pytest
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Plan, PlanAsset, Asset

@pytest.mark.django_db
def test_invplan_details_valid_plan():
    # Crear activos con valores únicos en symbol_tv
    asset1 = Asset.objects.create(symbol_yf='TSLA', symbol_tv='TSLA', name='Asset 1')
    asset2 = Asset.objects.create(symbol_yf='AAPL', symbol_tv='AAPL', name='Asset 2')

    # Crear un plan de ejemplo
    plan = Plan.objects.create(name='Plan 1', description='Description of Plan 1')

    # Asociar los activos al plan
    PlanAsset.objects.create(plan=plan, asset=asset1, percentage=50)
    PlanAsset.objects.create(plan=plan, asset=asset2, percentage=50)

    # Configurar cliente de API
    client = APIClient()

    # Hacer la solicitud GET al endpoint con el ID del plan creado (el ID del plan es el que se ha creado dinámicamente)
    response = client.get(f'/api/invplan/details/{plan.id}/')

    # Verificar que el código de estado es 200 OK
    assert response.status_code == status.HTTP_200_OK

    # Verificar que la respuesta contiene los campos esperados
    response_data = response.json()
    assert 'name' in response_data
    assert 'description' in response_data
    assert 'labels' in response_data
    assert 'percentages' in response_data

    # Verificar que los datos en 'labels' y 'percentages' son correctos
    assert response_data['labels'] == ['Asset 1', 'Asset 2']
    assert response_data['percentages'] == [50.0, 50.0]

# Test cuando el plan no existe (404 Not Found)
@pytest.mark.django_db
def test_invplan_details_plan_not_found():
    # Configurar cliente de API
    client = APIClient()

    # Hacer la solicitud GET con un ID de plan que no existe
    response = client.get('/api/invplan/details/9999/')  # Suponiendo que no existe un plan con ID 9999

    # Verificar que el código de estado es 404 Not Found
    assert response.status_code == status.HTTP_404_NOT_FOUND

# Test de un plan sin activos asociados
@pytest.mark.django_db
def test_invplan_details_no_assets():
    # Crear un plan sin activos asociados
    plan = Plan.objects.create(name='Plan Sin Activos', description='Este plan no tiene activos.')

    # Configurar cliente de API
    client = APIClient()

    # Hacer la solicitud GET al endpoint con el ID del plan
    response = client.get(f'/api/invplan/details/{plan.id}/')

    # Verificar que el código de estado es 200 OK
    assert response.status_code == status.HTTP_200_OK

    # Verificar que la respuesta contiene los campos esperados
    response_data = response.json()
    assert 'name' in response_data
    assert 'description' in response_data
    assert 'labels' in response_data
    assert 'percentages' in response_data

    # Verificar que las listas de labels y percentages están vacías
    assert response_data['labels'] == []
    assert response_data['percentages'] == []
