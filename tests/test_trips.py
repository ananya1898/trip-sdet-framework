def test_get_trips(client):
    response = client.get(client.base_url + "/trips")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_create_trip(client):
    trip_data = {
        "destination": "Paris",
        "budget": 1500.0
    }
    response = client.post(client.base_url + "/trips", json=trip_data)
    assert response.status_code == 200
    assert response.json()["trip"]["id"] != None
    assert response.json()["message"] == "Trip created successfully"
    assert response.json()["trip"]["destination"] == trip_data["destination"]
    assert response.json()["trip"]["budget"] == trip_data["budget"]
