import os
from dotenv import load_dotenv
load_dotenv()
from data_manager import DataManager

SERP_API = os.environ["SERP_API"]

data_manager = DataManager()
sheets_data = data_manager.get_data()
print(sheets_data)