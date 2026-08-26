
import pytest
from test_data.trip_data import VALID_TRIPS, INVALID_BUDGETS, INVALID_DESTINATIONS

#Postive test case for retrieving trips
@pytest.mark.smoke
def test_get_trips(trip_client):
    response = trip_client.get_trips()
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

#Positive test case for retrieving a specific trip
@pytest.mark.smoke  
def test_get_trip(trip_client,created_trip_cleanup):
    trip_data = {
        "destination": "New York",
        "budget": 2000.0
    }

    create_response = trip_client.create_trip(trip_data)

    assert create_response.status_code == 200

    trip_id = create_response.json()["trip"]["id"]
    created_trip_cleanup.append(trip_id)  # Cleanup: Add the created trip ID to the cleanup list for deletion after the test

    get_response = trip_client.get_trip(trip_id)

    assert get_response.status_code == 200
    data = get_response.json()
    assert data["trip"]["id"] == trip_id
    assert data["trip"]["destination"] == trip_data["destination"]
    assert data["trip"]["budget"] == trip_data["budget"]


#Positive test case for creating a trip
@pytest.mark.smoke
@pytest.mark.parametrize("trip_data", VALID_TRIPS)
def test_create_trip(trip_client,trip_data,created_trip_cleanup):

    response = trip_client.create_trip(trip_data)  

    assert response.status_code == 200
    data = response.json()

    #Cleanup: Add the created trip ID to the cleanup list for deletion after the test
    trip_id = data["trip"]["id"]
    created_trip_cleanup.append(trip_id)   
 
    assert data["trip"]["id"] is not None
    assert data["message"] == "Trip created successfully"
    assert data["trip"]["destination"] == trip_data["destination"]
    assert data["trip"]["budget"] == trip_data["budget"]



#Business rule valudation for creating a trip with invalid budget values
@pytest.mark.parametrize("budget", INVALID_BUDGETS)
@pytest.mark.regression
def test_create_trip_invalid_budget(trip_client,budget):
    trip_data = {
        "destination": "Paris",
        "budget": budget
    }
    response = trip_client.create_trip(trip_data)

    assert response.status_code == 422

#Value validation for creating a trip with empty destination
@pytest.mark.parametrize("destination", INVALID_DESTINATIONS)
@pytest.mark.regression 
def test_create_trip_empty_destination(trip_client,destination):
    trip_data = {
        "destination": destination,
        "budget": 1500.0
    }
    response = trip_client.create_trip(trip_data)
    assert response.status_code == 422 

#Required field validation for creating a trip with missing fields
@pytest.mark.parametrize("trip_data", [
    {"destination": "Paris"},  # Missing budget
    {"budget": 1500.0}  # Missing destination
])
@pytest.mark.regression 
def test_create_trip_missing_fields(trip_client, trip_data):
    response = trip_client.create_trip(trip_data)
    assert response.status_code == 422  

#Type validation for creating a trip with invalid data types
@pytest.mark.parametrize("trip_data", [
    {"destination": 123, "budget": 1500.0},  # Invalid destination type
    {"destination": "Paris", "budget": "not_a_number"}  # Invalid budget type
])
@pytest.mark.regression 
def test_create_trip_invalid_types(trip_client, trip_data):
    response = trip_client.create_trip(trip_data)
    assert response.status_code == 422  

#Non existent trip retrieval test case  
@pytest.mark.regression
def test_get_nonexistent_trip(trip_client):
    response = trip_client.get_trip(99999)  # Assuming 99999 is a non-existent trip ID
    assert response.status_code == 404
    assert response.json()["detail"] == "Trip not found"

#Non existent trip deletion test case                   
@pytest.mark.regression
def test_delete_nonexistent_trip(trip_client):
    response = trip_client.delete_trip(99999)  # Assuming 99999 is a non-existent trip ID
    assert response.status_code == 404
    assert response.json()["detail"] == "Trip not found" 

#Non existent trip update test case
@pytest.mark.regression 
def test_update_nonexistent_trip(trip_client):   
    updated_trip_data = {
        "destination": "Updated Destination",
        "budget": 2000.0
    }
    response = trip_client.update_trip(99999, updated_trip_data)  # Assuming 99999 is a non-existent trip ID
    assert response.status_code == 404
    assert response.json()["detail"] == "Trip not found"    

@pytest.mark.regression
def test_create_trip_persists_to_database(trip_client, db_client, created_trip_cleanup):

    trip_data = {
        "destination": "Database Test",
        "budget": 5000.0
    }

    response = trip_client.create_trip(trip_data)

    assert response.status_code == 200

    trip_id = response.json()["trip"]["id"]
    created_trip_cleanup.append(trip_id)  # Cleanup: Add the created trip ID to the cleanup list for deletion after the test


    query = """
        SELECT id, destination, budget
        FROM trips
        WHERE id = ?
    """

    result = db_client.execute_query(
        query,
        (trip_id,)
    )

    assert len(result) == 1
    assert result[0][0] == trip_id
    assert result[0][1] == trip_data["destination"]
    assert result[0][2] == trip_data["budget"]


@pytest.mark.regression
def test_update_trip_persists_to_database(trip_client, db_client, created_trip_cleanup):

    trip_data = {
        "destination": "Delhi",
        "budget": 5000.0
    }

    create_response = trip_client.create_trip(trip_data)

    assert create_response.status_code == 200

    trip_id = create_response.json()["trip"]["id"]

    updated_data = {
        "destination": "Mumbai",
        "budget": 8000.0
    }

    update_response = trip_client.update_trip(
        trip_id,
        updated_data
    )

    assert update_response.status_code == 200

    created_trip_cleanup.append(trip_id)  # Cleanup: Add the created trip ID to the cleanup list for deletion after the test


    query = """
        SELECT id, destination, budget
        FROM trips
        WHERE id = ?
    """

    result = db_client.execute_query(
        query,
        (trip_id,)
    )

    assert len(result) == 1
    assert result[0][0] == trip_id
    assert result[0][1] == updated_data["destination"]
    assert result[0][2] == updated_data["budget"]


@pytest.mark.regression
def test_delete_trip_persists_to_database(trip_client, db_client, created_trip_cleanup):

    trip_data = {
        "destination": "Bangalore",
        "budget": 6000.0
    }

    create_response = trip_client.create_trip(trip_data)

    assert create_response.status_code == 200

    trip_id = create_response.json()["trip"]["id"]
    created_trip_cleanup.append(trip_id)  # Cleanup: Add the created trip ID to the cleanup list for deletion after the test


    delete_response = trip_client.delete_trip(trip_id)

    assert delete_response.status_code == 200

    query = """
        SELECT id
        FROM trips
        WHERE id = ?
    """

    result = db_client.execute_query(
        query,
        (trip_id,)
    )

    assert len(result) == 0  