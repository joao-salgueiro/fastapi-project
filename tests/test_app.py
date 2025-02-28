from http import HTTPStatus
from fastapi.testclient import TestClient
import pytest
from fastapiplayground.app import app

client = TestClient(app)




def test_read_root_should_return_ok_and_hello_world(client):
    response = client.get('/') #act (action)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world'}

def test_read_root_should_return_a_html_page_with_hello_world(client):
     #Arrage - test organization
    response = client.get('/exer')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Hello Worldd</h1>' in response.text

def test_create_user():
    client = TestClient(app)

    response = client.post('/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1
    }

def test_read_users(client):
     response = client.get('/users/')
     assert response.status_code == HTTPStatus.OK
     assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }