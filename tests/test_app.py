from fastapi.testclient import TestClient
from app import app

# client = TestClient(app) #todo test precisa de cliente


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # arrange (organizzação)

    response = client.get("/")  # Ação

    assert response.status_code == 200
    assert response.json() == {"message": "Olá mundo"} #vericação de resposta esperada
