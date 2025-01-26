import requests
import helpers
import urls
import pytest


@pytest.fixture(scope='function')
def create_and_delete_user():
    payload = helpers.create_new_user_and_return_auth_data()
    yield payload
    response = requests.post(f'{urls.BASE_URL}{urls.NEW_USER_URL}', data=payload)
    access_token = response.json().get('accessToken')
    requests.delete(f'{urls.BASE_URL}{urls.DELETE_USER_URL}', headers={'Authorization': access_token})
