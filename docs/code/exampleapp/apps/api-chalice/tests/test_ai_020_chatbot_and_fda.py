"""
Test ai_chatbot and FDA endpoints
"""
import json
import pytest

from genericsuite.util.app_logger import log_debug

from tests.test_020_common import (
    get_default_headers,
)

from tests.test_ai_010_common import (
    ai_test_prepare,
)

# conversation is a json string comes from the frontend
# must be converted to a list of strings
# conversation = '[{"role": "user", "content": "give me the calories for broccoli"}]'
CONVERSATION_EN = '[{"role": "user", "content": "give me the calories for broccoli"}]'
body_chatbot_data = {
    "conversation": CONVERSATION_EN
}
body_fda_data = [
    {
        "food_name": "broccoli",
        "raw_result": "1",
    },
    {
        "food_name": "cheddar cheese",
    },
    {
        "food_name": "aaa$$%#$$%^#334#@85#$@#$",
    }
]


def test_ai_fda_prepare(client):
    """
    Test ai_chatbot endpoint preparation.
    """
    ai_test_prepare(client)


# @pytest.mark.skip(reason="no way of currently testing this")
def test_ai_chatbot_happy(client):
    """Test ai_chatbot endpoint."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/ai/chatbot',
        body=json.dumps(body_chatbot_data),
        headers=dict(headers)
    )
    assert hcr.status_code == 200

    json_data = hcr.json_body
    assert 'response' in json_data
    assert 'error' in json_data
    assert 'error_message' in json_data

    data = json_data['response']
    assert isinstance(data, str), "API response should be a string"
    assert "Broccoli" in data or "broccoli" in data or "BROCCOLI" in data
    assert "calorie" in data or "KCAL" in data or "Kcal" in data \
        or "kcal" in data


# @pytest.mark.skip(reason="no way of currently testing this")
def test_ai_chatbot_sad_401(client):
    """Sad test GET ai_chatbot: unauthorized."""

    headers = get_default_headers("bad_token")
    hcr = client.http.post(
        '/ai/chatbot',
        body=json.dumps(body_chatbot_data),
        headers=dict(headers)
    )
    assert hcr.status_code == 401


# @pytest.mark.skip(reason="no way of currently testing this")
def test_ai_chatbot_no_conversation(client):
    """Sad test GET ai_chatbot: no conversation provided."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/ai/chatbot',
        headers=dict(headers)
    )
    assert hcr.status_code == 400
    assert b'No conversation provided [AICC-E010]' in hcr.body


def test_fda_api_happy_raw(client):
    """Test FDA API endpoint."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/fda_food_query',
        body=json.dumps(body_fda_data[0]),
        headers=dict(headers)
    )
    assert hcr.status_code == 200

    json_data = hcr.json_body
    assert 'response' in json_data
    assert 'error' in json_data
    assert 'error_message' in json_data

    # 'response' has the response from the FDA API
    data = json_data['response']
    assert isinstance(data, dict), "API response should be a dict"
    assert 'foodSearchCriteria' in data
    assert 'query' in data['foodSearchCriteria']
    assert body_fda_data[0]["food_name"].lower() \
           in data['foodSearchCriteria']['query'].lower()


def test_fda_api_happy_calories(client):
    """Test FDA API endpoint."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/fda_food_query',
        body=json.dumps(body_fda_data[1]),
        headers=dict(headers)
    )
    assert hcr.status_code == 200

    json_data = hcr.json_body
    assert 'response' in json_data
    assert 'error' in json_data
    assert 'error_message' in json_data

    # 'resultset' has the response from calories()
    data = json_data['resultset']
    assert isinstance(data, list), "API response should be a list"
    assert 'description' in data[0]
    log_debug(f"Food description: {data[0]['description']}")
    assert body_fda_data[1]["food_name"].lower() + \
           ' has ' \
           in data[0]['description'].lower()
    assert 'KCAL' in data[0]['description']


def test_fda_api_not_found(client):
    """Test FDA API endpoint."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/fda_food_query',
        body=json.dumps(body_fda_data[2]),
        headers=dict(headers)
    )
    assert hcr.status_code == 400
