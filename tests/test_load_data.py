import pytest
from app.load_data import HikingRoutes

# Test 1
def test_HikingRoutes_file_path_can_only_be_str():
    with pytest.raises(ValueError):
        HikingRoutes(0)

# Test 2
def test_HikingRoutes_get_all_routes_method_returns_list_of_Hike_objects():
    test = HikingRoutes("/Users/leonievs/Documents/coding-projects/hiking-routes/app/data/routes.json")
    data = test.get_all_routes()
    assert isinstance(data, list)
  

