from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "/Users/timothyfisher/PycharmProjects/chromedriver-3"

s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

items = driver.find_element(By.CSS_SELECTOR, "#store")
all_items = items.find_elements(By.TAG_NAME, "div")

prices_and_ids = {}

for i in range(0,8):
    price = int(all_items[i].text.split("-")[1].split("\n")[0].replace(",",""))
    id = all_items[i].get_attribute("id")
    prices_and_ids[id] = price

print(prices_and_ids)

timeout = time.time() + 5
after_5 = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        cookie_count = driver.find_element(By.ID, "money").text.replace(",", "")
        print(cookie_count)

        for id, price in prices_and_ids.items():
            print(id,price)
            if int(cookie_count) >= price:
                time.sleep(0.1)
                driver.find_element(By.ID, id).click()
                print(f"{id} was bought")

    if time.time() > after_5:
        print(driver.find_element(By.ID, "cps").text)
        break