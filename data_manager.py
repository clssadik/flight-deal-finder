import os
from dotenv import load_dotenv
load_dotenv()
import requests
import requests_cache

class DataManager:
    
    def __init__(self):
        self.SHEETY_AUTH = os.environ["SHEETY_AUTH"]
        self.SHEETY_URL = "https://api.sheety.co/0473906867a46fc610805d81714a83fa/flightDeals/prices"
    
    def get_google_sheets_data(self):
        
        sheets_headers = {
            "Authorization" : self.SHEETY_AUTH,
        }

        requests_cache.install_cache('flight_cache', expire_after=3600)
        response = requests.get(url=self.SHEETY_URL,headers=sheets_headers)
        data = response.json()
        return data["prices"]