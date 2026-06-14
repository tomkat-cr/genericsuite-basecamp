"""
AI Chatbot test common methods
"""
import json
import pytest

from genericsuite.util.app_logger import log_debug

from tests.test_020_common import (
    get_default_headers,
    test_create_user,
    test_login,
)


# conversation is a json string comes from the frontend
# must be converted to a list of strings
# conversation = '[{"role": "user", "content": "give me the calories for broccoli"}]'
CONVERSATION_EN = '[{"role": "user", "content": "{question}"}]'
HANDLE_FDA_ERROR = ""
# HANDLE_FDA_ERROR = ". If the calorie information couldn't be retrieved" + \
#     " from the FDA database, search it on the Internet, and if it fails" + \
#     " too, deduce it from your model." + \
#     " If there is more than one option, in the FDA database, take the first one."
DONT_ASK_CONFIRMATION = ". Don't ask me for any confirmation or question," + \
    " just proceed with the information you gathered or have."
MODELS_TO_TEST = [
    # "chat_openai",
    # "huggingface",
    "gemini",
    # # "clarifai",
]

def ai_test_prepare(client):
    """
    Test ai_chatbot endpoint.
    """
    test_create_user(client)
    test_login(client)
    log_debug("TEST_AI_FDA_PREPARE" +
        f"\n | pytest.session_token: {pytest.session_token}" +
        f"\n | pytest.new_user_id: {pytest.new_user_id}" +
        "\n")
    assert pytest.session_token is not None
    assert pytest.new_user_id is not None


def ai_generic_test(client, test_input):
    """Test ai_chatbot endpoint with fixture data."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.post(
        '/ai/chatbot',
        body=json.dumps(test_input["body_chatbot_data"]),
        headers=dict(headers)
    )
    assert hcr.status_code == 200

    json_data = hcr.json_body
    assert 'response' in json_data
    assert 'error' in json_data
    assert 'error_message' in json_data

    data = json_data['response']
    assert isinstance(data, str), "API response should be a string"
    for expected_item in test_input["expected_response"]:
        assert expected_item.lower() in data.lower()
