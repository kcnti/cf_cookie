from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests

chromeOptions = Options()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("window-size=1920,1080")
chromeOptions.add_argument("--disable-popup-blocking")
chromeOptions.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67")
chromeOptions.add_argument("--disable-infobars")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chromeOptions)
driver.get(url)
time.sleep(10)
for req in driver.requests:
    try:
        print("#########################")
        print(req.url)
        print(req.headers)
        print(req.response.headers)
        print("#########################")
        print()
    except:
        print("#########################")
        print(req.url)
        print("#########################")
        continue
