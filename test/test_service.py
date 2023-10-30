"""Pytest Mocking Demo"""

from unittest import mock
import pytest
from requests.exceptions import HTTPError

from source import service


@mock.patch("source.service.get_user")
def test_get_user(mock_get_user):
    """Test getting user from database."""
    mock_get_user.return_value = "Mocked Alice"
    assert service.get_user(1) == "Mocked Alice"


@mock.patch("requests.get")
def test_get_user_from_api(mock_get):
    """Test getting user from API. Using mocking requests.get() as an example"""
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "Mocked Alice"}]
    mock_get.return_value = mock_response
    assert service.get_user_from_api() == [{"id": 1, "name": "Mocked Alice"}]


@mock.patch("requests.get")
def test_get_user_from_api_http_error(mock_get):
    """Test getting user from API. Using mocking requests.get() as an example in
    case of HTTPError"""
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    with pytest.raises(HTTPError):
        service.get_user_from_api()
