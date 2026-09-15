VALID_TRIPS = [
    {
        "destination": "Goa",
        "budget": 15000.0
    },
    {
        "destination": "Manali",
        "budget": 20000.0
    },
    {
        "destination": "Bali",
        "budget": 30000.0
    }
]


INVALID_BUDGETS = [
    -1,
    0
]


INVALID_DESTINATIONS = [
    "",
    "   ",
]


MISSING_FIELD_TRIPS = [
    {
        "destination": "Paris"
    },
    {
        "budget": 1500.0
    }
]


INVALID_TYPE_TRIPS = [
    {
        "destination": 123,
        "budget": 1500.0
    },
    {
        "destination": "Paris",
        "budget": "not_a_number"
    }
]


NON_EXISTENT_TRIP_ID = 99999


INVALID_TRIP_UPDATE = {
    "destination": "Updated Destination",
    "budget": 2000.0
}


DATABASE_UPDATE_TRIP = {
    "destination": "Mumbai",
    "budget": 5000.0
}