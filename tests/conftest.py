# precisa ter este nome
from fastapi.testclient import TestClient
from fast_zero.app import app

import pytest


# fixures
@pytest.fixture()
def client():
    return TestClient(app)  # arrange
