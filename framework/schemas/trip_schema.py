from pydantic import BaseModel


class TripData(BaseModel):
    id: int
    destination: str
    budget: float


class TripResponse(BaseModel):
    message: str
    trip: TripData

class GetTripResponse(BaseModel):
    trip: TripData