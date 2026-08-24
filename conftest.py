import pytest

from framework.api.clients.trip_client import TripClient
from framework.database.db_client import DatabaseClient

@pytest.fixture
def base_url():
    return "http://localhost:8000"

@pytest.fixture
def trip_client(base_url):
    return TripClient(base_url)

@pytest.fixture
def db_client():
    return DatabaseClient(
        r"D:\Projects\tripmate\tripmate.db"
    )