import pytest
import requests

EMAIL = 'olga@example.com'
PASSWORD = 'string1'
URL = 'http://restapi.adequateshop.com/api/AuthAccount/Login'


def test_login():
    """
    Test login API: Happy Path
    """
    body = {
        "email": EMAIL,
        "password": PASSWORD
    }
    response = requests.post(
        url = URL, 
        json = body, 
        headers = {
            'Content-Type': 'application/json'
            }
        )
    
    assert response.status_code == 200

    answer = response.json()
    assert answer['code'] == 0
    assert answer['message'] == 'success'
    assert answer['data']['Email'] == EMAIL


def test_login_empty_password():
    """
    Test login API: Empty password
    """
    body = {
        "email": EMAIL,
        "password": ''
    }
    response = requests.post(
        url = URL, 
        json = body, 
        headers = {
            'Content-Type': 'application/json'
            }
        )
    
    assert response.status_code == 400

    answer = response.json()
    assert answer['Message'] == 'The request is invalid.'

def test_login_empty_email():
    """
    Test login API: Empty email
    """
    body = {
        "email": '',
        "password": PASSWORD
    }
    response = requests.post(
        url = URL, 
        json = body, 
        headers = {
            'Content-Type': 'application/json'
            }
        )
    
    assert response.status_code == 400

    answer = response.json()
    assert answer['Message'] == 'The request is invalid.'

def test_login_empty_email_and_password():
    """
    Test login API: Empty email and empty password
    """
    body = {
        "email": '',
        "password": ''
    }
    response = requests.post(
        url = URL, 
        json = body, 
        headers = {
            'Content-Type': 'application/json'
            }
        )
    
    assert response.status_code == 400

    answer = response.json()
    assert answer['Message'] == 'The request is invalid.'

def test_login_wrong_password():
    """
    Test login API: Wrong password
    """
    body = {
        "email": EMAIL,
        "password": PASSWORD + '1'

    }
    response = requests.post(
        url = URL, 
        json = body, 
        headers = {
            'Content-Type': 'application/json'
            }
        )
    
    assert response.status_code == 200

    answer = response.json()
    assert answer['code'] == 1
    assert answer['message'] == 'invalid username or password'
    assert answer['data'] is None



def test_login_wrong_email():
    """
    Test login API: Wrong email
    """
    body = {
        "email": EMAIL + '1',
        "password": PASSWORD

    }
    response = requests.post(
        url = URL, 
        json = body, 
        headers = {
            'Content-Type': 'application/json'
            }
        )
    
    assert response.status_code == 200

    answer = response.json()
    assert answer['code'] == 1
    assert answer['message'] == 'invalid username or password'
    assert answer['data'] is None

