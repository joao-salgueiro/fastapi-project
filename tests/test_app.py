from http import HTTPStatus
from fastapi.testclient import TestClient

from fastapiplayground.app import app

client = TestClient(app)


def test_read_root_should_return_ok_and_hello_world():
    client = TestClient(app) #Arrage - test organization
    response = client.get('/') #act (action)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Message': 'Hello World'}