import pytest
import requests

@pytest.fixture
def client():
    session = requests.Session()
    session.base_url = "http://localhost:8000"  # Replace with your API base URL
    return session 