import pytest
from app.utils import HikingRoutes

# Test 1
def test_HikingRoutes_file_path_can_only_be_str():
    with pytest.raises(ValueError):
        HikingRoutes(0)