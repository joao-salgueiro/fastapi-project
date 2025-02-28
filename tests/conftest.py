from fastapi.testclient import TestClient
import pytest
from fastapiplayground.app import app


@pytest.fixture
def client():
    return TestClient(app)
