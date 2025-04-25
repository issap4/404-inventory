from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

URL = "https://404-inventory.streamlit.app/"

def ping_streamlit():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(URL)

        # Esperar hasta que el título de la página contenga "404 Material"
        WebDriverWait(driver, 60).until(
            EC.title_contains("404 Material")
        )

        print(f"[{datetime.utcnow()}] ✅ Page loaded: {URL}")
    except Exception as e:
        print(f"[{datetime.utcnow()}] ❌ Timed out or error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    ping_streamlit()
