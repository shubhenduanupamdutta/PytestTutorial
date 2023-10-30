"""Function for Pytest Mocking Demo"""
import requests

# Mock database
Users: dict[int, str] = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
    4: "Dave",
    5: "Eve"
}


def get_user(user_id: int) -> str:
    """Get user from database."""
    return Users[user_id]


def get_user_from_api() -> dict:
    """Get user from API."""
    response = requests.get("https://jsonplaceholder.typicode.com/users/", timeout=20)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError(f"Error {response.status_code}")
    return response.json()
