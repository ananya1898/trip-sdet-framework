import pytest

from framework.api.clients.trip_client import TripClient
from framework.database.db_client import DatabaseClient



@pytest.fixture
def client():
    return TripClient("http://localhost:8000")

@pytest.fixture
def db_client():
    return DatabaseClient(
        r"D:\Projects\tripmate\tripmate.db"
    )