import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture(scope="module")
def api_session():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session

def test_fluxo_completo_petstore(api_session):
    # 1. USER: Criar usuário
    user_payload = {
        "id": 9876,
        "username": "qa_user",
        "firstName": "QA",
        "lastName": "Tester",
        "email": "qa@test.com",
        "password": "12345",
        "phone": "99999999",
        "userStatus": 1
    }
    response_user = api_session.post(f"{BASE_URL}/user", json=user_payload)
    assert response_user.status_code == 200
    assert response_user.json()["code"] == 200

    # 2. PET: Incluir um novo pet
    pet_payload = {
        "id": 12345,
        "name": "Rex",
        "status": "available"
    }
    response_pet = api_session.post(f"{BASE_URL}/pet", json=pet_payload)
    assert response_pet.status_code == 200
    assert response_pet.json()["name"] == "Rex"
    assert response_pet.json()["status"] == "available"

    # 3. STORE: Realizar pedido de um pet
    order_payload = {
        "id": 1,
        "petId": 12345,
        "quantity": 1,
        "shipDate": "2026-05-27T21:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    response_order = api_session.post(f"{BASE_URL}/store/order", json=order_payload)
    assert response_order.status_code == 200
    assert response_order.json()["petId"] == 12345
    assert response_order.json()["status"] == "placed"