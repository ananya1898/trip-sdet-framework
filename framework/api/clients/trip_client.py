from .base_client import BaseClient


class TripClient(BaseClient):

    def create_trip(self, trip_data):
        return self.post("/trips", json=trip_data)

    def get_trips(self):
        return self.get("/trips")

    def get_trip(self, trip_id):
        return self.get(f"/trips/{trip_id}")

    def update_trip(self, trip_id, trip_data):
        return self.put(
            f"/trips/{trip_id}",
            json=trip_data
        )

    def delete_trip(self, trip_id):
        return self.delete(f"/trips/{trip_id}")