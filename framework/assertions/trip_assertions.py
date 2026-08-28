def assert_trip(trip_response, expected_trip):

    trip = trip_response.trip

    assert trip.id == expected_trip["id"]
    assert trip.destination == expected_trip["destination"]
    assert trip.budget == expected_trip["budget"]