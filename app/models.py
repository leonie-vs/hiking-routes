from pydantic import BaseModel
from typing import List

class PublicTransportRoute(BaseModel):
    mode: List[str]
    departure: str
    arrival: str
    changes: int
    travel_time_minutes: int

class DurationHours(BaseModel):
    min: float
    max: float 

class Hike(BaseModel):
    id: int
    name: str
    from_location: str
    to_location: str
    route_start_point: str
    public_transport_route: List[PublicTransportRoute]
    distance_km: float
    duration_hours: DurationHours
    elevation_m: int
    pubs_on_route: bool

