"""
Test ai_chatbot and user dishes.
"""
import os
import pytest

from tests.test_ai_010_common import (
    ai_test_prepare,
    ai_generic_test,
    CONVERSATION_EN,
    HANDLE_FDA_ERROR,
    DONT_ASK_CONFIRMATION,
    MODELS_TO_TEST,
)


TEST_DATA = [
    {
        "body_chatbot_data": {
            "conversation": CONVERSATION_EN.replace('{question}',
                "give me an apple pie recipe and add it to my dishes" +
                " with the name 'apple pie'. If" +
                " there is more than one recipe options, give me just" +
                " the first one." + HANDLE_FDA_ERROR + DONT_ASK_CONFIRMATION),
        },
        "expected_response": [
            # I've successfully added the "Perfect Apple Pie" to your dishes, based on the recipe found on Pillsbury.com. This classic dessert is made in three simple steps using Pillsbury Pie Crusts and includes ingredients such as apples, lemon juice, sugar, flour, cinnamon, salt, and nutmeg. Enjoy baking!
            "apple pie",
            "recipe",
            "added",
            "to",
            "your",
            "dishes",
        ],
    },
    {
        "body_chatbot_data": {
            "conversation": CONVERSATION_EN.replace('{question}',
                "Is humble pie in my dishes?"),
        },
        "expected_response": [
            # It looks like "humble pie" is not in your list of dishes.
            "no",
            "humble pie",
            "your",
            "dishes",
        ],
    },
    {
        "body_chatbot_data": {
            "conversation": CONVERSATION_EN.replace('{question}',
                "Is apple pie in my dishes?"),
        },
        "expected_response": [
            "yes",
            "apple pie",
            "is",
            "your",
            "dishes",
        ],
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
        ai_generic_test(client, test_input)
