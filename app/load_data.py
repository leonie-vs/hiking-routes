import json
from app.models import Hike
from pathlib import Path

# class to extract all data from routes.json
class HikingRoutes:
    
    def __init__(self, file_path: str):
        if not isinstance(file_path, str):
            raise ValueError("filepath must be a string")
        self.file_path = Path(file_path)
    
    def get_all_routes(self):
        with self.file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return [Hike(**h) for h in data]
