import shodan 
import os
from typing import List, Dict

class ShodanService:
    def __init__(self):
        self.api_key = os.getenv("SHODAN_API_KEY")
        if not self.api_key:
            raise EnvironmentError("Falta la API Key de Shodan (variable SHODAN_API_KEY)")
        self.api = shodan.Shodan(self.api_key)

    def search(self, query: str = "DVWA") -> List[Dict]:
        try:
            results = self.api.search(query)
            parsed_results = []
            for result in results['matches']:
                parsed_results.append({
                    "ip": result['ip_str'],
                    "port": result['port'],
                    "organization": result.get('org', 'N/A'),
                    "banner": result['data']
                })
            return parsed_results
        except shodan.APIError as e:
            return [{"error": f"Shodan API Error: {str(e)}"}]