import pytest
import requests
from datetime import datetime
import random
import string

NAME = 'Luce'
EMAIL = 'luce@example.com'
LOCATION = 'heaven'
URL = 'http://restapi.adequateshop.com/api/Tourist'


def _get_random_email(base_email):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(5))
    return f'{result_str}{base_email}'

def _create_tourist(name, email, location):
    response = requests.post(
        url = URL, 
        json = {
            "id": 0,
            "tourist_name": name,
            "tourist_email": email,
            "tourist_location": location,
            "createdat": datetime.now().isoformat()
        }, 
        headers = {
            'Content-Type': 'application/json'
            }
        )
    
    assert response.status_code == 201
    return response.json()['id']


def test_get_tourist():
    """
    GET Tourist: Happy Path
    """
    email = _get_random_email(EMAIL)
    tourist_id = _create_tourist(NAME, email, LOCATION)
    response = requests.get(url = f'{URL}/{tourist_id}')
    assert response.status_code == 200
    answer = response.json()
    assert answer['id'] == tourist_id
    assert answer['tourist_name'] == NAME
    assert answer['tourist_email'] == email
    assert answer['tourist_location'] == LOCATION


def _delete_tourist(tourist_id):
    response = requests.delete(url = f'{URL}/{tourist_id}')
    
    assert response.status_code == 200
    return response.json()['id']

def test_get_lost_tourist():
    """
    GET Tourist: Tourist does not exist
    """
    # API is broken and does not allow DELETE method and I can't be sure that a tourist with random Id does not exist
    pytest.skip("API is broken")
    email = _get_random_email(EMAIL)
    tourist_id = _create_tourist(NAME, email, LOCATION)
    _delete_tourist(tourist_id)
    response = requests.get(url = f'{URL}/{tourist_id}')
    assert response.status_code == 404
