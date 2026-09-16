
import pytest

from framework.api.clients.trip_client import TripClient
from framework.config.config import DATABASE_PATH
from framework.config.config import BASE_URL
from framework.database.db_client import DatabaseClient
from framework.utils.logger import get_logger
from framework.database.trip_repository import TripRepository
from test_data.trip_factory import create_trip_data

logger = get_logger(__name__)

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def trip_client(base_url):
    return TripClient(base_url)

@pytest.fixture
def db_client():
    return DatabaseClient(DATABASE_PATH)

@pytest.fixture
def created_trip_cleanup(trip_repository):
    created_trip_ids = []

    yield created_trip_ids

    for trip_id in created_trip_ids:
        trip_repository.delete_trip(trip_id)
        logger.info(f"Deleted trip with ID: {trip_id} from the database.")

@pytest.fixture
def existing_trip(trip_client, created_trip_cleanup):
    trip_data = create_trip_data()

    response = trip_client.create_trip(trip_data)

    assert response.status_code == 200

    trip = response.json()["trip"]

    created_trip_cleanup.append(trip["id"])

    return trip

@pytest.fixture
def trip_repository(db_client):
    return TripRepository(db_client)