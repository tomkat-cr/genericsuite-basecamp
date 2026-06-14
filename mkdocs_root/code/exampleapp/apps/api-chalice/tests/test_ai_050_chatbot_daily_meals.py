"""
Test ai_chatbot and user ingredients, dishes and daily meals
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
                "give me a 250g hamburger calories and add it to my" +
                " today\'s meals at lunch" + HANDLE_FDA_ERROR +
                DONT_ASK_CONFIRMATION),
        },
        "expected_response": [
            # I've successfully added a 250g hamburger, estimated at 1282.5 calories, to your lunch for today.
            # The 250g hamburger has been estimated to contain approximately 1283.5 calories and has been successfully added to today's meals at lunch.
            "250g",
            "hamburger",
            "added",
            "to",
            "today",
            "lunch",
        ],
    },
    {
        "body_chatbot_data": {
            "conversation": CONVERSATION_EN.replace('{question}',
                "what I ate today at lunch?"),
        },
        "expected_response": [
            # For lunch today, you had a Hamburger, which contained 625.88 calories. This meal was a 250g serving.
            "250g",
            "hamburger",
            "lunch",
            "today",
        ],
    },
    {
        "body_chatbot_data": {
            "conversation": CONVERSATION_EN.replace('{question}',
                "what I ate yesterday at lunch?"),
        },
        "expected_response": [
            # It appears there were no recorded meals for your account on 2024-02-25 at lunchtime. You might not have logged your meal, or there could be a mistake in the date or meal time entry. If you'd like to log a meal for that day or need assistance with anything else, please let me know!
            # It seems like there's no record of what you ate for lunch yesterday. You might not have logged your meal, or perhaps it was an oversight. Would you like to log it now or need help with something else?
            # It looks like there were no meals recorded for lunch on 2024-03-01. If you did have a meal but forgot to log it, you might want to add it now for accurate tracking of your dietary intake.
            "no",
            "meals",
            "lunch",
            "record",
            # "yesterday",
        ],
    },
]


def test_ai_daily_meals_prepare(client):
    """
    Test ai_chatbot endpoint.
    """
    ai_test_prepare(client)


@pytest.mark.parametrize("test_input", TEST_DATA)
def test_ai_daily_meals_chatbot(client, test_input):
    """
    Test ai_chatbot endpoint with fixture data.
    """
    ai_generic_test(client, test_input)
