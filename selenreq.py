from selenium import webdriver
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
time.sleep(30)
driver.refresh()
time.sleep(30)
driver_cookie = driver.get_cookies()
cookie = ""

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"en-US,en;q=0.9",
    "cache-control":"max-age=0",
    "sec-ch-ua":'"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
}

cookies = {}
for cookie in driver.get_cookies():
    cookies[cookie['name']] = cookie['value']

print(cookies)

r = requests.get(url, headers=headers, cookies=cookies)
print(r)

