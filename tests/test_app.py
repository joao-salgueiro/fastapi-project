from http import HTTPStatus
from fastapi.testclient import TestClient
import pytest
from fastapiplayground.app import app

client = TestClient(app)


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
     
def test_read_users_by_invalid_id(client):
    response = client.get('/users/35')
    assert response.status_code == HTTPStatus.NOT_FOUND
     
def test_read_users_by_id(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
       
            
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
            
        
    } 


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
                'password': '123',
                'username': 'testeusername2',
                'email': 'test@example.com',
                'id': 1,    
        })
    
    assert response.json() == {
                'username': 'testeusername2',
                'email': 'test@example.com',
                'id': 1,    
        }

def test_update_user_passing_a_invalid_id(client):
    response = client.put(
        '/users/35',
        json={
            'password': '123',
                'username': 'testeusername2',
                'email': 'test@example.com',
                'id': 1,  
        }
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}

def test_delete_users(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}

def test_delete_user_passing_a_invalid_id(client):
    response = client.delete('/users/35')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}