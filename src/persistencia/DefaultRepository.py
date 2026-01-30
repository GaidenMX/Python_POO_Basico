
import json
import os

class DefaultRepository:

    def __init__(self, filename: str):
        self.filepath = os.path.join(os.path.dirname(__file__), "..", "..", "data", filename)
        # Aseguramos que la carpeta /data exista
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def guardar_datos(self, data: list):
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def cargar_datos(self) -> list:
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, 'r') as f:
            return json.load(f)
        