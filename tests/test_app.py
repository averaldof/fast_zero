from http import HTTPStatus


# client = TestClient(app)
# #todo test precisa de client
def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")  # Ação

    assert response.status_code == 200
    assert response.json() == {"message": "Olá mundo"}  # vericação de resposta esperada


# post test
def test_create_user(client):

    response = client.post(
        "/users/",
        json={"username": "fulano", "password": "1234", "email": "arroba@mail.com"},
    )
    # Validação Status
    assert response.status_code == HTTPStatus.CREATED
    # Validação UserPublic
    assert response.json() == {
        "username": "fulano",
        "email": "arroba@mail.com",
        "id": 1,
    }


# get test
def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "fulano",
                "email": "arroba@mail.com",
                "id": 1,
            }
        ]
    }


# put test
def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "password": "1234",
            "username": "ex-fulano",
            "email": "testeput@mail.com",
            "id": 1,
        },
    )

    assert response.json() == {
        "username": "ex-fulano",
        "email": "testeput@mail.com",
        "id": 1,
    }


# delete
def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.json() == {"message": "Usuário deletado"}
