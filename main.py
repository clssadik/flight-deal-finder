import os
from dotenv import load_dotenv
load_dotenv()
import requests

SERP_API = os.environ["SERP_API"]
SHEETY_AUTH = os.environ["SHEETY_AUTH"]
SHEETY_URL = "https://api.sheety.co/0473906867a46fc610805d81714a83fa/flightDeals/prices"
