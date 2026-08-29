"""
Test ai_chatbot and user ingredients
"""
import pytest

from tests.test_ai_010_common import (
    ai_test_prepare,
    ai_generic_test,
    CONVERSATION_EN,
    HANDLE_FDA_ERROR,
    DONT_ASK_CONFIRMATION,
)

TEST_DATA = [
    {
        "body_chatbot_data": {
            "conversation": CONVERSATION_EN.replace('{question}',
                "give me the 250g hamburger calories and add it to my" +
                " ingredients." + HANDLE_FDA_ERROR + DONT_ASK_CONFIRMATION),
        },
        # I've successfully added the hamburger with a serving size of 250g and 294.11 kcal to your ingredients.
        "expected_response": [
            "250g",
            "hamburger",
            "added",
            "to",
            "your",
            "ingredients",
        ],
    },
    {
        "body_chatbot_data": {
            "conversation": CONVERSATION_EN.replace('{question}',
                "Is pineapple in my ingredients?"),
        },
        # Final Answer: It looks like pineapple is not currently listed in your ingredients.
        "expected_response": [
            "no",
            "pineapple",
            "your",
            "ingredients",
        ],
    },
    {
        "body_chatbot_data": {
            "conversation": CONVERSATION_EN.replace('{question}',
                "Is 250g hamburger in my ingredients?"),
        },
        "expected_response": [
            "yes",
            "250g",
            "hamburger",
            "is",
            "in",
            "your",
            "ingredients",
        ],
    },
]


def test_ai_ingredients_prepare(client):
    """
    Test ai_chatbot endpoint.
    """
    ai_test_prepare(client)


@pytest.mark.parametrize("test_input", TEST_DATA)
def test_ai_ingredients_chatbot(client, test_input):
    """
    Test ai_chatbot endpoint with fixture data.
    """
    ai_generic_test(client, test_input)
