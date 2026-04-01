from app.models import Hike

def filter_by_max_travel_time(hikes: list[Hike], max_travel_time: int) -> list[Hike]:
    """Return hikes where at least one public transport route is within the max travel time."""
    return [
        hike for hike in hikes
        if any(
            route.travel_time_minutes <= max_travel_time
            for route in hike.public_transport_route
        )
    ]