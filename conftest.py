
import pytest

from framework.api.clients.trip_client import TripClient
from framework.database.db_client import DatabaseClient
from framework.utils.logger import get_logger

logger = get_logger(__name__)

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

@pytest.fixture
def created_trip_cleanup(db_client):
    created_trip_ids = []

    yield created_trip_ids

    for trip_id in created_trip_ids:
        db_client.execute_update(
            "DELETE FROM trips WHERE id = ?",
            (trip_id,)
        )
        logger.info(f"Deleted trip with ID: {trip_id} from the database.")