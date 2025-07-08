"""
Test ai_chatbot and webpage analyzer.
"""
import os
import pytest

from tests.test_ai_010_common import (
    ai_test_prepare,
    ai_generic_test,
    CONVERSATION_EN,
    MODELS_TO_TEST,
)

TEST_URLS = [
    {
        "url": "https://huggingface.co/blog/inference-pro",
        "expected_response": [
            "1234",
        ],

    }
]
TEST_DATA = [
    {
        "body_chatbot_data": {
            "conversation": CONVERSATION_EN.replace('{question}',
                #  "give me a summary of this web page: " +
                "does it worth to get the pro subscription ? accorting to this web page: " +
                "{WEBPAGE_URL}"
            ),
        },
        "expected_response": [],
    },
]


def test_ai_dishes_prepare(client):
    """
    Test ai_chatbot endpoint.
    """
    ai_test_prepare(client)


@pytest.mark.parametrize("test_input", TEST_DATA)
def test_ai_dishes_chatbot(client, test_input):
    """
    Test ai_chatbot endpoint with fixture data.
    """
    for model in MODELS_TO_TEST:
        os.environ["LANGCHAIN_DEFAULT_MODEL"] = model
        for url in TEST_URLS:
            test_input_url = test_input.copy()
            test_input_url["body_chatbot_data"]["conversation"] = \
                test_input_url["body_chatbot_data"]["conversation"].replace(
                    "{WEBPAGE_URL}", url["url"]
                )
            test_input_url["expected_response"] = url["expected_response"]
            ai_generic_test(client, test_input_url)
