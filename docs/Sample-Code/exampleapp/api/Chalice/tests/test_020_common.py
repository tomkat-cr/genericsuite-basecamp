"""
User's testing common properties and methods
"""
import json
import os
import datetime
import base64
import requests

import jwt
import pytest

from genericsuite.util.passwords import Passwords
from genericsuite.util.app_logger import log_debug

HTTP_USE_REQUESTS = False
HTTP_DEFAULT_TIMEOUT = 10
HTTP_SERVER_URL = os.environ.get("HTTP_SERVER_URL", "http://localhost")

# HEADER_TOKEN_ENTRY_NAME = 'x-access-tokens'
HEADER_TOKEN_ENTRY_NAME = 'Authorization'

TEST_EMAIL = 'foo@baz.com'
TEST_PASSWORD = 'Q12!K34$j56_79'
DUMMY_USER_ID = '64bc28a962dee6a75d757845'
DUMMY_CREATION_DATE = 1635033994

test_users_record = {
    'firstname': 'Testy',
    'lastname': 'Testerson',
    'passcode': TEST_PASSWORD,
    # 'creation_date': 1635033994,
    'birthday': -131760000,
    'email': TEST_EMAIL,
    'gender': 'm',
    'height': '1.70',
    'height_unit': 'm',
    'weight': '74',
    'weight_unit': 'kg',
    'training_days': 'MTWXFS',
    'training_hour': '17:00',
    'pytest_run': 1,
    "superuser": False,
    "status": "1",
    # "plan": "basic",  # Uses GPT-3.5
    "plan": "premium",  # Uses GPT-4
    "goal_code": "",
    "goals": "",
    "language": "en",
}

TEST_FOOD_MOMENT_ID = '6174cf3e31d0f78fb73abf54'

# ----- Utilities BEGIN


def get_request(client):
    """
    Returns the current request object
    """
    request = client.current_request
    return request


def get_id_as_string_in_test(row):
    """
    Returns the id as string in test
    """
    if "$oid" in row['_id']:
        return str(row["_id"]["$oid"])
    return str(row['_id'])


def get_default_headers(token):
    """
    Returns the default headers with Authorization Bearer
    """
    headers = {
        "content-type": "application/json",
        HEADER_TOKEN_ENTRY_NAME: f'Bearer {token}'
    }
    return headers


def token_encode(user):
    """
    Returns the encoded JWT token
    """
    app_secret_key = os.environ['APP_SECRET_KEY']
    token = jwt.encode(
        {
            'public_id': str(user['_id']),
            'exp':
                datetime.datetime.utcnow() +
                datetime.timedelta(minutes=30)
        },
        app_secret_key,
        algorithm="HS256"
    )
    log_debug('TEST TOKEN_ENCODE' +
              # f' | app_secret_key: {app_secret_key}' +
              f' | token: {token}' +
              f' | user: {user}')
    return token


def get_valid_default_headers():
    """
    Returns the valid default headers with Authorization Bearer
    """
    user = {'_id': DUMMY_USER_ID}
    token = token_encode(user)
    headers = get_default_headers(token)
    return headers


def get_default_resultset():
    """
    Returns the default resultset
    """
    resultset = {
        'error': False,
        'error_message': None,
        'totalPages': None,
        'resultset': {}
    }
    return resultset


def fetch_user_by_email(client, email):
    """
    Returns the user by email
    """
    headers = get_valid_default_headers()
    hcr = client.http.get(
        # '/users?email={}'.format(email), headers=dict(headers)
        f'/users?email={email}', headers=dict(headers)
    )
    if hcr.status_code != 200:
        json_data_raw = get_default_resultset()
        json_data_raw['error'] = True
        json_data_raw['error_message'] = str(hcr.status_code)
    else:
        try:
            json_data_raw = hcr.json_body
        except BaseException as err:
            json_data_raw = get_default_resultset()
            json_data_raw['error'] = True
            json_data_raw['error_message'] = str(err)
    return json_data_raw


def delete_user(client, user_id):
    """
    Delete a user by id
    """
    headers = get_valid_default_headers()
    hcr = client.http.delete(
        # '/users/?id={}'.format(id), headers=dict(headers)
        f'/users/?id={user_id}', headers=dict(headers)
    )
    return hcr


def clean_test_user(client):
    """
    Clean the test user
    """
    json_data_raw = fetch_user_by_email(client, TEST_EMAIL)
    if json_data_raw['error']:
        return
    json_data = json.loads(json_data_raw['resultset'])
    delete_user(client, get_id_as_string_in_test(json_data))


def login_and_set_session_token(client):
    """
    Login and set session token
    """
    auth = {
        'username': test_users_record['email'],
        'password': test_users_record['passcode'],
    }
    valid_credentials = base64.b64encode(
        # str.encode("{}:{}".format(auth['username'], auth['password']))
        str.encode(f"{auth['username']}:{auth['password']}")
    ).decode("utf-8")
    log_debug("1) LOGIN_AND_SET_SESSION_TOKEN" +
        f"\n | auth: {auth}"
        f"\n | valid_credentials: {valid_credentials}"
    )
    url = f'{HTTP_SERVER_URL}/users/login'
    headers = {"Authorization": "Basic " + valid_credentials}
    if HTTP_USE_REQUESTS:
        headers['Content-Type'] ='application/json'
        log_debug("2.1) LOGIN_AND_SET_SESSION_TOKEN" +
            f"\n | url: {url}" +
            f"\n | headers: {headers}" +
            "\n")
        hcr = requests.post(
            url=url,
            headers=headers,
            json={},    # This fix the error HTTP 502
            timeout=HTTP_DEFAULT_TIMEOUT,
        )
    else:
        log_debug("2.2) LOGIN_AND_SET_SESSION_TOKEN" +
            f"\n | Use client (not URL): {client}" +
            f"\n | headers: {headers}" +
            "\n")
        hcr = client.http.post(
            url,
            headers=headers,
        )
    log_debug("3) LOGIN_AND_SET_SESSION_TOKEN" +
              f"\n | hcr.status_code: {hcr.status_code}" +
              "\n")
    pytest.session_token = None
    if hcr.status_code == 200:
        if HTTP_USE_REQUESTS:
            json_data = hcr.json()
        else:
            json_data = hcr.json_body
        if 'token' in json_data.get('resultset', {}):
            pytest.session_token = json_data['resultset']['token']
    log_debug("4) LOGIN_AND_SET_SESSION_TOKEN" +
              f"\n | pytest.session_token: {pytest.session_token}" +
              "\n")


# ----- Utilities END


def test_create_user(client):
    """
    Test Users creation.
    """
    clean_test_user(client)
    headers = get_valid_default_headers()
    hcr = client.http.post(
        '/users',
        headers=dict(headers),
        body=json.dumps(test_users_record),
    )
    psw_class = Passwords()

    assert hcr.status_code == 200
    json_data = hcr.json_body
    assert 'resultset' in json_data
    assert '_id' in json_data['resultset']
    pytest.new_user_id = json_data['resultset']['_id']
    assert pytest.new_user_id is not None
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'

    # Fetch the new user to verify created attributes
    hcr = client.http.get(
        # '/users?id={}'.format(pytest.new_user_id), headers=dict(headers)
        f'/users?id={pytest.new_user_id}', headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data_raw = hcr.json_body
    assert 'resultset' in json_data_raw
    json_data = json.loads(json_data_raw['resultset'])
    assert '_id' in json_data
    assert {'$oid': pytest.new_user_id} == json_data['_id']
    assert 'firstname' in json_data
    assert test_users_record['firstname'] == json_data['firstname']
    assert 'lastname' in json_data
    assert test_users_record['lastname'] == json_data['lastname']
    assert 'passcode' in json_data
    assert psw_class.verify_password(json_data['passcode'],
                                     test_users_record['passcode'])
    assert 'creation_date' in json_data
    assert 'update_date' in json_data


def test_login(client):
    """
    Test user login.
    """
    log_debug("TEST_LOGIN")
    auth = {
        'username': test_users_record['email'],
        'password': test_users_record['passcode'],
    }
    valid_credentials = base64.b64encode(
        # str.encode("{}:{}".format(auth['username'], auth['password']))
        str.encode(f"{auth['username']}:{auth['password']}")
    ).decode("utf-8")
    hcr = client.http.post(
        '/users/login',
        headers={"Authorization": "Basic " + valid_credentials}
    )
    assert b'Could not verify' not in hcr.body
    assert hcr.status_code == 200
    json_data = hcr.json_body
    assert 'token' in json_data['resultset']
    # global_data['session_token'] = json_data['resultset']['token']
    pytest.session_token = json_data['resultset']['token']
