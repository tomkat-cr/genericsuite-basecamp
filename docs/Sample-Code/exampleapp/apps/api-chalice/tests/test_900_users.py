"""
Users table tests
"""
import json
import os
import base64

import pytest

from genericsuite.util.passwords import Passwords

from tests.test_020_common import (
    fetch_user_by_email,
    delete_user,
    TEST_EMAIL,
    TEST_PASSWORD,
    TEST_FOOD_MOMENT_ID,
    test_users_record,
    get_default_headers,
    DUMMY_CREATION_DATE,
    get_id_as_string_in_test,
    login_and_set_session_token,
    test_create_user,
    test_login,
    # get_request,
)


def test_create_superadmin_user(client):
    """Test super-admin User creation."""

    supad_username = os.environ['APP_SUPERADMIN_EMAIL']
    supad_password = os.environ['APP_SECRET_KEY']
    json_data_raw = fetch_user_by_email(client, supad_username)
    if not json_data_raw['error']:
        json_data = json.loads(json_data_raw['resultset'])
        delete_user(client, get_id_as_string_in_test(json_data))

    auth = {
        'username': supad_username,
        'password': supad_password,
    }
    valid_credentials = base64.b64encode(
        str.encode("{}:{}".format(auth['username'], auth['password']))
    ).decode("utf-8")
    hcr = client.http.post(
        '/users/supad-create',
        headers={"Authorization": "Basic " + valid_credentials}
    )
    assert hcr.status_code == 200


def test_create_superadmin_user_fail(client):
    """Test super-admin User creation."""

    auth = {
        'username':
            os.environ.get('APP_SUPERADMIN_EMAIL', 'foo_admin@bar.com'),
        'password': TEST_PASSWORD,
    }
    valid_credentials = base64.b64encode(
        str.encode("{}:{}".format(auth['username'], auth['password']))
    ).decode("utf-8")
    hcr = client.http.post(
        '/users/supad-create',
        headers={"Authorization": "Basic " + valid_credentials}
    )
    assert hcr.status_code == 400
    assert b'Could not verify [SAC3]' in hcr.body \
        or b'User already exists [SAC4]' in hcr.body


def test_connection(client):
    """Test connection by querying the collections list (tables)."""

    if not pytest.session_token:
        login_and_set_session_token(client)
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.get('/users/test', headers=dict(headers))
    assert hcr.status_code == 200
    json_data = hcr.json_body
    assert 'resultset' in json_data
    assert 'collections' in json_data['resultset']
    assert 'users' in json_data['resultset']['collections']


def test_create_user_again(client):
    """Test fail trying to create the test user again."""

    if not pytest.new_user_id:
        test_create_user(client)
        test_login(client)

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/users',
        body=json.dumps(dict(test_users_record)),
        headers=dict(headers)
    )
    assert hcr.status_code == 400
    assert bytes(
        'User ' + TEST_EMAIL + ' already exists [CU4]', 'utf-8'
    ) in hcr.body


def test_fetch_users_list(client):
    """Test Users list."""

    headers = get_default_headers(pytest.session_token)
    page = 1
    limit = 1
    hcr = client.http.get(
        # '/users?page={}&limit={}'.format(1, 0), headers=dict(headers)
        f'/users?page={page}&limit={limit}',
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data_raw = hcr.json_body
    # {
    #   'error': False,
    #   'error_message': None,
    #   'resultset': '[{"_id": {"$oid": "6234804f0990244c025c599c"},' +
    #       '"birthday": -1317...1.70", "tall_unit": "meters",' +
    #       '"training_days": "MTWXFS", "training_hour": "17:00",' +
    #       '"update_date": 1647607887.898997}]'
    # }
    assert 'resultset' in json_data_raw
    json_data = json.loads(json_data_raw['resultset'])
    assert isinstance(json_data, list)
    assert len(json_data) > 0
    assert 'firstname' in json_data[0]
    assert 'lastname' in json_data[0]
    assert 'passcode' not in json_data[0]
    assert 'creation_date' in json_data[0]
    # assert 'update_date' in json_data[0]
    row_to_compare = dict(test_users_record)
    del row_to_compare['passcode']
    row_found = list(
        filter(
            lambda user: user['email'] == row_to_compare['email'], json_data
        )
    )
    assert len(row_found) == 1


def test_fetch_user(client):
    """Test fetch one user by its id."""

    headers = get_default_headers(pytest.session_token)
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


def get_user(client):
    """Get user data by ID."""
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.get(
        f'/users?id={pytest.new_user_id}',
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data_raw = hcr.json_body
    assert 'resultset' in json_data_raw
    json_data = json.loads(json_data_raw['resultset'])
    json_data["_id"] = get_id_as_string_in_test(json_data)
    return json_data


def test_update_users(client):
    """Test update some user data."""
    # psw_class = Passwords(get_request(client=client))
    psw_class = Passwords()

    updated_record = get_user(client)
    updated_record['firstname'] = 'My Name'
    updated_record['lastname'] = 'Is Groot'
    updated_record['passcode'] = '87654321'

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.put(
        '/users', body=json.dumps(updated_record), headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data = hcr.json_body
    # {'error': False, 'error_message': '',
    #   'resultset': {'rows_affected': '1'}
    # }
    assert 'resultset' in json_data
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'

    # Fetch the updated user to verify updated attributes
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
    assert updated_record['firstname'] == json_data['firstname']
    assert 'lastname' in json_data
    assert updated_record['lastname'] == json_data['lastname']
    assert 'passcode' in json_data
    assert psw_class.verify_password(json_data['passcode'],
                                     updated_record['passcode'])
    assert 'creation_date' in json_data
    # assert 'update_date' in json_data


def test_failed_update_users_creation_date(client):
    """Test failed update user becasue missing creation_date."""
    updated_record = dict(test_users_record)
    updated_record['_id'] = pytest.new_user_id
    updated_record['firstname'] = 'My Name'
    updated_record['lastname'] = 'Is Groot'
    updated_record['passcode'] = '87654321'

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.put(
        '/users', body=json.dumps(updated_record), headers=dict(headers)
    )
    assert hcr.status_code == 400


def test_failed_update_users(client):
    """Test failed update some user data."""

    updated_record = dict(test_users_record)
    del updated_record['weight']
    del updated_record['weight_unit']
    updated_record['_id'] = pytest.new_user_id
    updated_record['firstname'] = 'Jose'
    updated_record['lastname'] = 'Divo'
    updated_record['passcode'] = '87654321'

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.put(
        '/users', body=json.dumps(updated_record), headers=dict(headers)
    )
    assert hcr.status_code == 400
    #
    # {'error': True, 'error_message': 'Missing mandatory elements:
    #   weight,  weight_unit [UU1].', 'resultset': {}
    # }
    # json_data = hcr.json_body
    # assert 'resultset' in json_data
    # assert 'error' in json_data
    # assert json_data['resultset']['error'] == True
    # assert 'error_message' in json_data
    # assert json_data['resultset']['error_message'] == \
    #   'Missing mandatory elements:  weight,  weight_unit [UU1]'
    # assert 'resultset' in json_data
    # assert json_data['resultset'] == {}
    #
    # Missing mandatory elements: weight_unit, weight [UU1]
    # Missing mandatory elements: weight, weight_unit [UU1]
    assert (
        b'Missing mandatory elements:' in hcr.body and
        b'weight_unit' in hcr.body and
        b'weight' in hcr.body and
        b'creation_date' in hcr.body and
        b'[UU1]' in hcr.body
    )


# ----- food_times


def test_add_food_times_to_user(client):
    """Test add a food_times item to the test user."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/users_food_times',
        body=json.dumps(
            {
                'user_id': pytest.new_user_id,
                'food_times':
                    {
                        'food_moment_id': TEST_FOOD_MOMENT_ID,
                        'food_time': '12:00'
                    }
            }
        ),
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data = hcr.json_body
    # {'error': False, 'error_message': None,
    #   'resultset': {'rows_affected': '1'}
    # }
    assert 'resultset' in json_data
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'


def test_fetch_food_times_from_user(client):
    """Test food_times list."""

    headers = get_default_headers(pytest.session_token)
    page = 1
    limit = 1
    hcr = client.http.get(
        '/users_food_times?page={}&limit={}&user_id={}'.format(
            1, 1, pytest.new_user_id
        ),
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data_raw = hcr.json_body
    assert 'resultset' in json_data_raw
    json_data = json.loads(json_data_raw['resultset'])
    assert isinstance(json_data, list)
    assert len(json_data) == 1
    assert 'food_moment_id' in json_data[0]
    assert 'food_time' in json_data[0]
    assert json_data[0] == {
        'food_moment_id': TEST_FOOD_MOMENT_ID,
        'food_time': '12:00'
    }


def test_update_food_times_to_user(client):
    """Test update a food_times item in the test user."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.put(
        '/users_food_times',
        body=json.dumps(
            {
                'user_id': pytest.new_user_id,
                'food_times':
                    {
                        'food_moment_id': TEST_FOOD_MOMENT_ID,
                        'food_time': '22:00'
                    }
            }
        ),
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data = hcr.json_body
    # {'error': False, 'error_message': None,
    #   'resultset': {'rows_affected': '1'}
    # }
    assert 'resultset' in json_data
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'


def test_create_dup_food_times_to_user(client):
    """Test create a duplicate food_times item in the test user."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/users_food_times',
        body=json.dumps(
            {
                'user_id': pytest.new_user_id,
                'food_times':
                    {
                        'food_moment_id': TEST_FOOD_MOMENT_ID,
                        'food_time': '22:00'
                    }
            }
        ),
        headers=dict(headers)
    )
    assert hcr.status_code == 400
    # HTTP status: 400
    # Response body:
    #   Food moment 6174cf3e31d0f78fb73abf54 already exist [AFTTU3]
    assert (
        bytes(
            'Food Time ' + TEST_FOOD_MOMENT_ID + ' already exist [AFTTU3]',
            'UTF8'
        ) in hcr.body
    )


def test_remove_food_times_to_user(client):
    """Test delete a food_times item from the test user."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.delete(
        '/users_food_times',
        body=json.dumps(
            {
                'user_id': pytest.new_user_id,
                'food_times': {
                    'food_moment_id': TEST_FOOD_MOMENT_ID
                }
            }
        ),
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data = hcr.json_body
    assert 'resultset' in json_data
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'


# ----- user_history


def test_add_user_history_to_user(client):
    """Test add a user_history item to the test user."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/users_user_history',
        body=json.dumps(
            {
                'user_id': pytest.new_user_id,
                'user_history':
                    {
                        'date': DUMMY_CREATION_DATE,
                        'goals': 'Loose weight',
                        'weight': '70',
                        'weight_unit': 'kg'
                    }
            }
        ),
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data = hcr.json_body
    assert 'resultset' in json_data
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'


def test_fetch_user_history_from_user(client):
    """Test user_history list."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.get(
        '/users_user_history?page={}&limit={}&user_id={}'.format(
            1, 1, pytest.new_user_id
        ),
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data_raw = hcr.json_body
    assert 'resultset' in json_data_raw
    json_data = json.loads(json_data_raw['resultset'])
    assert isinstance(json_data, list)
    assert len(json_data) == 1
    assert 'date' in json_data[0]
    assert 'goals' in json_data[0]
    assert 'weight' in json_data[0]
    assert 'weight_unit' in json_data[0]
    assert json_data[0] == {
        'date': DUMMY_CREATION_DATE,
        'goals': 'Loose weight',
        'weight': '70',
        'weight_unit': 'kg'
    }


def test_update_user_history_to_user(client):
    """Test update a user_history item to the test user."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.put(
        '/users_user_history',
        body=json.dumps(
            {
                'user_id': pytest.new_user_id,
                'user_history':
                    {
                        'date': DUMMY_CREATION_DATE,
                        'goals': 'Get fit',
                        'weight': '82',
                        'weight_unit': 'kg'
                    }
            }
        ),
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data = hcr.json_body
    assert 'resultset' in json_data
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'


def test_remove_user_history_to_user(client):
    """Test delete a user_history item from the test user."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.delete(
        '/users_user_history',
        body=json.dumps(
            {
                'user_id': pytest.new_user_id,
                'user_history': {
                    'date': DUMMY_CREATION_DATE,
                }
            }
        ),
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data = hcr.json_body
    assert 'resultset' in json_data
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'


# ----- Sprint cleaning


def test_delete_user(client):
    """Test delete the test user."""

    assert pytest.new_user_id is not None
    assert pytest.session_token is not None
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.delete(
        '/users/?id={}'.format(pytest.new_user_id), headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data = hcr.json_body
    # {'error': False, 'error_message': None,
    #   'resultset': {'rows_affected': '1'}
    # }
    assert 'resultset' in json_data
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'


def test_delete_user_again(client):
    """Test fail trying to delete the test user again."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.delete(
        '/users/?id={}'.format(pytest.new_user_id), headers=dict(headers)
    )
    assert hcr.status_code == 400
    # error: User 62348adbfbe27f42c4837015 doesn't exist [DU1].
    assert b'error: User ' in hcr.body and b'doesn\'t exist [DU1]' in hcr.body
