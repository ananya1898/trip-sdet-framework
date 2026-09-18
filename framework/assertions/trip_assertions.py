def assert_trip(trip_response, expected_trip):

    trip = trip_response.trip

    assert trip.id == expected_trip["id"]
    assert trip.destination == expected_trip["destination"]
    assert trip.budget == expected_trip["budget"]


def assert_trip_matches_request(trip_response, request_data):

    trip = trip_response.trip

    assert trip.destination == request_data["destination"]
    assert trip.budget == request_data["budget"]