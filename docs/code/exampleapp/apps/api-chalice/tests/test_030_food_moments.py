"""
Food moments test
"""
import json
import pytest
import requests

from tests.test_020_common import (
    get_default_headers,
    get_default_resultset,
    get_valid_default_headers,
    get_id_as_string_in_test,
    test_create_user,
    login_and_set_session_token,
    HTTP_SERVER_URL,
    HTTP_DEFAULT_TIMEOUT,
    HTTP_USE_REQUESTS,
)

from genericsuite.util.app_logger import log_debug

test_food_moments_record = {
    'name': "Breakfast",
}

# ----- Utilities BEGIN


def fetch_food_moment_by_name(client, name):
    """
    Fetch food moment by name
    """
    log_debug(f"FETCH_FOOD_MOMENT_BY_NAME | name: {name}")
    headers = get_valid_default_headers()
    hcr = client.http.get(
        # '/food_moments?name={}'.format(name), headers=dict(headers)
        f'/food_moments?name={name}', headers=dict(headers)
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


def delete_food_moment(client, fm_id):
    """
    Delete food_moment
    """
    log_debug("DELETE_FOOD_MOMENT")
    headers = get_valid_default_headers()
    hcr = client.http.delete(
        # '/food_moments/?id={}'.format(id), headers=dict(headers)
        f'/food_moments/?id={fm_id}', headers=dict(headers)
    )
    return hcr


def clean_test_food_moment(client):
    """
    Clean test food moment
    """
    log_debug("CLEAN_TEST_FOOD_MOMENT")
    json_data_raw = fetch_food_moment_by_name(
        client, test_food_moments_record['name']
    )
    if json_data_raw['error']:
        return
    json_data = json.loads(json_data_raw['resultset'])
    delete_food_moment(client, str(json_data['_id']['$oid']))

# ----- Utilities END


def test_create_food_moment(client):
    """
    Test food_moment creation.
    """
    log_debug("1) TEST_CREATE_FOOD_MOMENT" +
              f"\n | HTTP_SERVER_URL: {HTTP_SERVER_URL}" +
              f"\n | Food Moment record: {test_food_moments_record}")
    if not pytest.session_token:
        test_create_user(client)
        login_and_set_session_token(client)
    clean_test_food_moment(client)
    headers = get_default_headers(pytest.session_token)
    log_debug("1.1) TEST_CREATE_FOOD_MOMENT" +
              f"\n | headers: {headers}")
    if HTTP_USE_REQUESTS:
        hcr = requests.post(
            f'{HTTP_SERVER_URL}/food_moments',
            json=test_food_moments_record,
            headers=dict(headers),
            timeout=HTTP_DEFAULT_TIMEOUT,
        )
    else:
        hcr = client.http.post(
            '/food_moments',
            body=json.dumps(test_food_moments_record),
            headers=dict(headers)
        )
    # Verify creation was OK
    log_debug("1.2) TEST_CREATE_FOOD_MOMENT" + 
              f"\n | Post result (status_code): {hcr.status_code}" + 
              "\n | json_body: " +
              f"{hcr.json() if HTTP_USE_REQUESTS else hcr.json_body}")
    assert hcr.status_code == 200
    if HTTP_USE_REQUESTS:
        json_data = hcr.json()
    else:
        json_data = hcr.json_body
    assert 'resultset' in json_data
    assert '_id' in json_data['resultset']
    pytest.new_food_moment_id = json_data['resultset']['_id']
    assert pytest.new_food_moment_id is not None
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'
    log_debug("2) TEST_CREATE_FOOD_MOMENT" +
              f" | Food Moment ID: {pytest.new_food_moment_id}")
    # Verify attributes of new food_moment
    hcr = client.http.get(
        # '/food_moments?id={}'.format(pytest.new_food_moment_id),
        f'/food_moments?id={pytest.new_food_moment_id}',
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data_raw = hcr.json_body
    assert 'resultset' in json_data_raw
    json_data = json.loads(json_data_raw['resultset'])
    log_debug("3) TEST_CREATE_FOOD_MOMENT" +
              f" | resultset: {json_data_raw['resultset']}")
    assert '_id' in json_data
    assert {'$oid': pytest.new_food_moment_id} == json_data['_id']
    assert 'name' in json_data
    assert test_food_moments_record['name'] == json_data['name']
    assert 'passcode' not in json_data
    assert 'update_date' in json_data
    assert 'creation_date' in json_data


def test_create_food_moment_again(client):
    """
    Test fail trying to create the test food_moment again.
    """
    log_debug("TEST_CREATE_FOOD_MOMENT_AGAIN")
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/food_moments',
        body=json.dumps(test_food_moments_record),
        headers=dict(headers)
    )
    assert hcr.status_code == 400
    assert bytes(
        'Food Moment ' + test_food_moments_record['name'] +
        ' already exists [CU4]', 'utf-8'
    ) in hcr.body


def test_fetch_food_moments_list(client):
    """
    Test food_moments list.
    """
    log_debug("TEST_FETCH_FOOD_MOMENTS_LIST")
    headers = get_default_headers(pytest.session_token)
    page = 1
    limit = 1
    hcr = client.http.get(
        # '/food_moments?page={}&limit={}'.format(1, 1),
        f'/food_moments?page={page}&limit={limit}',
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data_raw = hcr.json_body
    # {
    #   'error': False,
    #   'error_message': None,
    #   'resultset': '[{"_id": {"$oid": "6234804f0990244c025c599c"},' +
    #   ' "name": "Breakfast", "creation_date": 1647607887.898997,' +
    #   ' "update_date": 1647607887.898997}]'
    # }
    assert 'resultset' in json_data_raw
    json_data = json.loads(json_data_raw['resultset'])
    assert isinstance(json_data, list)
    assert len(json_data) == 1
    assert 'name' in json_data[0]
    assert 'passcode' not in json_data[0]
    assert 'update_date' in json_data[0]
    assert 'creation_date' in json_data[0]


def test_fetch_food_moment(client):
    """
    Test fetch one food_moment by its id.
    """
    log_debug("TEST_FETCH_FOOD_MOMENT")
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.get(
        # '/food_moments?id={}'.format(pytest.new_food_moment_id),
        f'/food_moments?id={pytest.new_food_moment_id}',
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data_raw = hcr.json_body
    assert 'resultset' in json_data_raw
    json_data = json.loads(json_data_raw['resultset'])
    assert '_id' in json_data
    assert {'$oid': pytest.new_food_moment_id} == json_data['_id']
    assert 'name' in json_data
    assert test_food_moments_record['name'] == json_data['name']
    assert 'passcode' not in json_data


def get_food_moments(client):
    """
    Get food_moments data by ID.
    """
    log_debug("GET_FOOD_MOMENTS")
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.get(
        # '/food_moments?id={}'.format(pytest.new_food_moment_id),
        f'/food_moments?id={pytest.new_food_moment_id}',
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data_raw = hcr.json_body
    assert 'resultset' in json_data_raw
    json_data = json.loads(json_data_raw['resultset'])
    json_data["_id"] = get_id_as_string_in_test(json_data)
    return json_data


def test_update_food_moments(client):
    """
    Test update some food_moment data.
    """
    log_debug("TEST_UPDATE_FOOD_MOMENTS")
    updated_record = get_food_moments(client)
    updated_record['name'] = 'Lunch'
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.put(
        '/food_moments',
        body=json.dumps(updated_record),
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data = hcr.json_body
    # {
    #   'error': False,
    #   'error_message': '',
    #   'resultset': {'rows_affected': '1'}
    # }
    assert 'resultset' in json_data
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'
    # Verify attributes of updated food_moment
    hcr = client.http.get(
        # '/food_moments?id={}'.format(pytest.new_food_moment_id),
        f'/food_moments?id={pytest.new_food_moment_id}',
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data_raw = hcr.json_body
    assert 'resultset' in json_data_raw
    json_data = json.loads(json_data_raw['resultset'])
    assert '_id' in json_data
    assert {'$oid': pytest.new_food_moment_id} == json_data['_id']
    assert 'name' in json_data
    assert updated_record['name'] == json_data['name']
    assert 'passcode' not in json_data
    assert 'update_date' in json_data
    assert 'creation_date' in json_data


def test_failed_update_food_moments_no_creation_date(client):
    """
    Test failed update food_moment without creation_date.
    """
    log_debug("TEST_FAILED_UPDATE_FOOD_MOMENTS_NO_CREATION_DATE")
    updated_record = dict(test_food_moments_record)
    updated_record['_id'] = pytest.new_food_moment_id
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.put(
        '/food_moments',
        body=json.dumps(updated_record),
        headers=dict(headers)
    )
    assert hcr.status_code == 400


def test_failed_update_food_moments(client):
    """
    Test failed update some food_moment data.
    """
    log_debug("TEST_FAILED_UPDATE_FOOD_MOMENTS")
    updated_record = dict(test_food_moments_record)
    del updated_record['name']
    updated_record['_id'] = pytest.new_food_moment_id
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.put(
        '/food_moments',
        body=json.dumps(updated_record),
        headers=dict(headers)
    )
    assert hcr.status_code == 400
    assert (
        b'Missing mandatory elements:' in hcr.body and
        b'name' in hcr.body and
        b'creation_date' in hcr.body and
        b'[UU1]' in hcr.body
    )


# ----- Spring cleaning


def test_delete_food_moment(client):
    """
    Test delete the test food_moment.
    """
    log_debug("TEST_DELETE_FOOD_MOMENT")
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.delete(
        # '/food_moments?id={}'.format(pytest.new_food_moment_id),
        f'/food_moments?id={pytest.new_food_moment_id}',
        headers=dict(headers)
    )
    assert hcr.status_code == 200
    json_data = hcr.json_body
    # {
    #   'error': False,
    #   'error_message': None,
    #   'resultset': {'rows_affected': '1'}
    # }
    assert 'resultset' in json_data
    assert 'rows_affected' in json_data['resultset']
    assert json_data['resultset']['rows_affected'] == '1'


def test_delete_food_moment_again(client):
    """
    Test fail trying to delete the test food_moment again.
    """
    log_debug("TEST_DELETE_FOOD_MOMENT_AGAIN")
    headers = get_default_headers(pytest.session_token)
    hcr = client.http.delete(
        # '/food_moments?id={}'.format(pytest.new_food_moment_id),
        f'/food_moments?id={pytest.new_food_moment_id}',
        headers=dict(headers)
    )
    assert hcr.status_code == 400
    # error: Food Moment 62348adbfbe27f42c4837015 doesn't exist [DU1].
    assert b'error: Food Moment ' in hcr.body \
        and b'doesn\'t exist [DU1]' in hcr.body
