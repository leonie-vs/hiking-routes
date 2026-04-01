from app.load_data import HikingRoutes
from app.services import filter_by_max_travel_time

def test_filter_by_max_travel_time_returns_only_matching_hikes():
    routes = HikingRoutes("app/data/routes.json").get_all_routes()
    result = filter_by_max_travel_time(routes, 60)

    assert len(result) == 1
    assert result[0].name == "Dovestone Reservoir Circular - The Trinnacles and Saddleworth Moor"