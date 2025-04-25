from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import chromedriver_autoinstaller

URL = "https://404-inventory.streamlit.app/"

def ping_streamlit():
    # Instala automáticamente el chromedriver compatible
    chromedriver_autoinstaller.install()

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    try:
        WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        print(f"[{datetime.utcnow()}] Fully loaded: {URL}")
    except:
        print(f"[{datetime.utcnow()}] Timed out loading: {URL}")
    finally:
        driver.quit()

if __name__ == "__main__":
    ping_streamlit()
