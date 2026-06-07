import os
from dotenv import load_dotenv
load_dotenv()
from data_manager import DataManager
from pprint import pprint

SERP_API = os.environ["SERP_API"]

data_manager = DataManager()
sheets_data = data_manager.get_data()
pprint(sheets_data)