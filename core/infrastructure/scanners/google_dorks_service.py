# core/infrastructure/services/google_service.py

import os
import requests

class GoogleDorkService:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.cse_id = os.getenv("CUSTOM_SEARCH_ENGINE_ID")
        self.base_url = "https://www.googleapis.com/customsearch/v1"

        if not self.api_key or not self.cse_id:
            raise ValueError("Faltan variables de entorno para Google API")

    def search(self, query: str, num_results: int = 5):
        params = {
            "q": query,
            "key": self.api_key,
            "cx": self.cse_id,
            "num": num_results
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json().get("items", [])
       