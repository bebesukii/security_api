# core/infrastructure/services/google_service.py

from core.domain.services import GoogleDorkServicePort
from core.domain.entities import GoogleDorkQuery
import requests
import os

class GoogleDorkService(GoogleDorkServicePort):
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.cse_id = os.getenv("CUSTOM_SEARCH_ENGINE_ID")
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def search(self, query: str, num_results: int = 5):
        validated_query = GoogleDorkQuery(query, num_results)
        params = {
            "q": validated_query.query,
            "key": self.api_key,
            "cx": self.cse_id,
            "num": validated_query.num_results
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json().get("items", [])
       
