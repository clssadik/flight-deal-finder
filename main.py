import os
from dotenv import load_dotenv
load_dotenv()
from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta


SERP_API = os.environ["SERP_API"]

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=182)

data_manager = DataManager()
sheets_data = data_manager.get_google_sheets_data()

# pprint(sheets_data)