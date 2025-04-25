# ping_app.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

URL = "https://404-inventory.streamlit.app/"

def ping_streamlit():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    print(f"[{datetime.utcnow()}] Accessed {URL}")
    driver.quit()

if __name__ == "__main__":
    ping_streamlit()
