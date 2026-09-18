
import pytest
from framework.database import trip_repository
from test_data.trip_data import (
    VALID_TRIPS,
    INVALID_BUDGETS,
    INVALID_DESTINATIONS,
    MISSING_FIELD_TRIPS,
    INVALID_TYPE_TRIPS,
    NON_EXISTENT_TRIP_ID,
    INVALID_TRIP_UPDATE,
    DATABASE_UPDATE_TRIP
)
from framework.assertions.trip_assertions import assert_trip, assert_trip_matches_request
from framework.schemas.trip_schema import TripResponse, GetTripResponse

#Postive test case for retrieving trips
@pytest.mark.smoke
def test_get_trips(trip_client):
    response = trip_client.get_trips()
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

#Positive test case for retrieving a specific trip
@pytest.mark.smoke  
def test_get_trip(trip_client, existing_trip):
    trip_id = existing_trip["id"]
    response = trip_client.get_trip(trip_id)
    data = response.json()
    assert response.status_code == 200
    trip_response = GetTripResponse.model_validate(data)
    assert_trip(trip_response, existing_trip)

#Positive test case for creating a trip
@pytest.mark.smoke
@pytest.mark.parametrize("trip_data", VALID_TRIPS)
def test_create_trip(trip_client,trip_data,created_trip_cleanup):

    response = trip_client.create_trip(trip_data)  

    assert response.status_code == 200
    data = response.json()
    trip_response = TripResponse.model_validate(data)

    #Cleanup: Add the created trip ID to the cleanup list for deletion after the test
    trip_id = data["trip"]["id"]
    created_trip_cleanup.append(trip_id)   

    assert_trip_matches_request(trip_response, trip_data)
    assert trip_response.message == "Trip created successfully"



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
@pytest.mark.parametrize("trip_data", MISSING_FIELD_TRIPS)
@pytest.mark.regression 
def test_create_trip_missing_fields(trip_client, trip_data):
    response = trip_client.create_trip(trip_data)
    assert response.status_code == 422  

#Type validation for creating a trip with invalid data types
@pytest.mark.parametrize("trip_data", INVALID_TYPE_TRIPS)
@pytest.mark.regression 
def test_create_trip_invalid_types(trip_client, trip_data):
    response = trip_client.create_trip(trip_data)
    assert response.status_code == 422  

#Non existent trip retrieval test case  
@pytest.mark.regression
def test_get_nonexistent_trip(trip_client):
    response = trip_client.get_trip(NON_EXISTENT_TRIP_ID)
    assert response.status_code == 404
    assert response.json()["detail"] == "Trip not found"

#Non existent trip deletion test case                   
@pytest.mark.regression
def test_delete_nonexistent_trip(trip_client):
    response = trip_client.delete_trip(NON_EXISTENT_TRIP_ID)
    assert response.status_code == 404
    assert response.json()["detail"] == "Trip not found" 

#Non existent trip update test case
@pytest.mark.regression 
def test_update_nonexistent_trip(trip_client):   
    updated_trip_data = INVALID_TRIP_UPDATE
    response = trip_client.update_trip(NON_EXISTENT_TRIP_ID, updated_trip_data)  # Assuming NON_EXISTENT_TRIP_ID is a non-existent trip ID
    assert response.status_code == 404
    assert response.json()["detail"] == "Trip not found"    

@pytest.mark.regression
def test_create_trip_persists_to_database(trip_client, trip_repository, existing_trip):

    trip_id = existing_trip["id"]

    response = trip_client.get_trip(trip_id)

    assert response.status_code == 200

    trip = trip_repository.get_trip(trip_id)

    assert trip is not None
    assert trip["id"] == trip_id
    assert trip["destination"] == existing_trip["destination"]
    assert trip["budget"] == existing_trip["budget"]


@pytest.mark.regression
def test_update_trip_persists_to_database(trip_client, trip_repository, existing_trip):

    trip_id = existing_trip["id"]

    updated_data = DATABASE_UPDATE_TRIP
    
    update_response = trip_client.update_trip(trip_id, updated_data)
    
    assert update_response.status_code == 200
    
    trip = trip_repository.get_trip(trip_id)
    assert trip is not None
    assert trip["id"] == trip_id
    assert trip["destination"] == updated_data["destination"]
    assert trip["budget"] == updated_data["budget"]

@pytest.mark.regression
def test_delete_trip_persists_to_database(trip_client, trip_repository, existing_trip):

    trip_id = existing_trip["id"]

    delete_response = trip_client.delete_trip(trip_id)

    assert delete_response.status_code == 200

    assert not trip_repository.trip_exists(trip_id)