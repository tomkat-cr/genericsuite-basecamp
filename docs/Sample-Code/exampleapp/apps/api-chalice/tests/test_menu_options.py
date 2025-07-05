import pytest

from tests.test_020_common import (
    get_default_headers,
)


def test_menu_options(client):
    """Test GET menu_options."""

    headers = get_default_headers(pytest.session_token)
    hcr = client.http.get(
        '/menu_options',
        headers=dict(headers)
    )
    assert hcr.status_code == 200

    json_data = hcr.json_body
    assert 'resultset' in json_data
    assert 'error' in json_data
    assert 'error_message' in json_data

    data = json_data['resultset']
    assert isinstance(data, list), "API response should be a list"

    for item in data[:2]:
        assert 'title' in item, "title attribute must exist"
        if 'location' in item:
            assert 'location' in item, "location attribute must exist"
        if 'type' in item:
            assert 'type' in item, "type attribute must exist"
            if item['type'] in ['editor']:
                assert 'element' in item, "element attribute must exist"
        assert isinstance(item['title'], str), "title attribute should be a string"
        assert isinstance(item['location'], str), "title attribute should be a string"
        assert isinstance(item['type'], str), "title attribute should be a string"
        if 'hard_prefix' in item:
            assert isinstance(item['hard_prefix'], bool), "hard_prefix attribute should be a boolean"
        if 'sub_menu_options' in item:
            assert isinstance(item['sub_menu_options'], list), "sub_menu_options attribute should be a list"


def test_menu_options_sad(client):
    """Sad test GET menu_options."""

    headers = get_default_headers("bad_token")
    hcr = client.http.get(
        '/menu_options',
        headers=dict(headers)
    )
    assert hcr.status_code == 401
