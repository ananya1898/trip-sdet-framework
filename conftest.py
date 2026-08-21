import pytest

from framework.api.clients.trip_client import TripClient


@pytest.fixture
def client():
    return TripClient("http://localhost:8000")