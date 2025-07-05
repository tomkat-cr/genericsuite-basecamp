"""
Tests configuration
"""
import pytest

from chalice.test import Client

from app import app

from genericsuite.util.app_logger import log_debug


@pytest.fixture
def client():
    """
    Chalice test client
    """
    log_debug("Chalice test CLIENT")
    with Client(app) as testing_client:
        yield testing_client


def pytest_configure():
    """
    Set up global variables for tests
    """
    pytest.session_token = None
    pytest.new_user_id = None
    pytest.new_food_moment_id = None
    pytest.ai_conversation_id = None
