import os
from dotenv import load_dotenv
load_dotenv()
import requests

class DataManager:
    
    def __init__(self):
        pass
    
    def get_data(self):
        SHEETY_AUTH = os.environ["SHEETY_AUTH"]
        SHEETY_URL = "https://api.sheety.co/0473906867a46fc610805d81714a83fa/flightDeals/prices"

        sheets_headers = {
            "Authorization" : SHEETY_AUTH,
        }

        response = requests.get(url=SHEETY_URL,headers=sheets_headers)
        data = response.json()
        return data["prices"]