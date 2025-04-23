import requests
from datetime import datetime

URL = "https://404-inventory.streamlit.app/"

try:
    response = requests.get(URL)
    print(f"[{datetime.now()}] Pinged {URL} - Status: {response.status_code}")
except Exception as e:
    print(f"[{datetime.now()}] Failed to ping {URL} - Error: {e}")
