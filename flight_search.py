from main import load_dotenv,os
load_dotenv()
import serpapi
import requests_cache


class FlightSearch:

    def __init__(self):
        self.API = os.environ["SERP_API"]

    def get_search_data(self):
        requests_cache.install_cache('flight_cache', expire_after=3600)

        client = serpapi.Client(api_key=self.API)
        results = client.search({
            for i in range(1,3):{
                
            }
                "engine": "google_flights",
                "departure_id": "COV",
                "arrival_id": "AUS",
                "currency": "USD",
                "type": "2",
                "outbound_date": "2026-06-07"
        })
        best_flights = results["best_flights"]