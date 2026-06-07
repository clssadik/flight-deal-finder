from main import load_dotenv,os
load_dotenv()
import serpapi

class FlightSearch:

    def __init__(self):
        self.API = os.environ["SERP_API"]

    def get_search_data(self):
        client = serpapi.Client(api_key=self.API)
        results = client.search({
            "engine": "google_flights",
            "departure_id": "CDG",
            "arrival_id": "AUS",
            "currency": "USD",
            "type": "2",
            "outbound_date": "2026-06-07"
        })
        best_flights = results["best_flights"]