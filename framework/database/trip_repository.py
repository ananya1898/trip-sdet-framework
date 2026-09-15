from unittest import result

from framework.database.db_client import DatabaseClient


class TripRepository:

    def __init__(self, db_client: DatabaseClient):
        self.db_client = db_client

    def get_trip(self, trip_id):
        query = """
            SELECT id, destination, budget
            FROM trips
            WHERE id = ?
        """

        result = self.db_client.execute_query(
            query,
            (trip_id,)
        )

        if not result:
            return None

        return {
            "id": result[0][0],
            "destination": result[0][1],
            "budget": result[0][2]
        }

    def trip_exists(self, trip_id):
        query = """
            SELECT 1
            FROM trips
            WHERE id = ?
        """

        result = self.db_client.execute_query(
            query,
            (trip_id,)
        )

        return len(result) > 0