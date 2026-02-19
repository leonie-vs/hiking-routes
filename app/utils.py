import json

class HikingRoutes:
    
    def __init__(self, file_path: str):
        if not isinstance(file_path, str):
            raise ValueError("filepath must be a string")
        self.file_path = file_path
    