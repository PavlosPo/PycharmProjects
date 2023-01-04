from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Any key on the keyboard

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://sso.teachable.com/secure/37913/identity/login/password")
#
# # article_count = driver.find_element(by='css selector', value='#articlecount a')
# # article_count.click()
#
# # all_portals = driver.find_element(by='link text', value="Contents")
# # all_portals.click()
#
# search_bar = driver.find_element(by=By.NAME, value="email")
# search_bar.send_keys("paulospoulos6@gmail.com")
# # search_bar.send_keys(Keys.TAB)
# search_bar = driver.find_element(by=By.NAME, value="password")
# search_bar.send_keys("fakepassword")
# search_bar.send_keys(Keys.ENTER)

# Cookie Game

import datetime
from selenium.webdriver.support.ui import WebDriverWait


def wait_to_load_language_box(driver):
    element = driver.find_element(by=By.ID, value="langSelect-EN")
    if element:
        return element
    else:
        return False

def buy_things(current_time, driver=driver):
    until_time = current_time + datetime.timedelta(seconds=5)
    if current_time > until_time:
        for i in range(0, 19, -1):
            print("Working 0")
            try:
                item = driver.find_element(by=By.ID, value=f"product{i}")
                item.click()
                break
            except:
                continue
        current_time = datetime.datetime.now()
    elif current_time < until_time:
        print("Working 1")
    else:
        print("notworking")

# Initial Driver
driver.get("https://orteil.dashnet.org/cookieclicker/")
# Waiting to find the Language Box Selection
element = WebDriverWait(driver, 5).until(wait_to_load_language_box)
# Finds the element and clicks it
element.click()
# Finds the cookie
cookie = driver.find_element(by=By.ID, value="bigCookie")

current_time = datetime.datetime.now()
for i in range(1, 10000000):
    buy_things(current_time)
    cookie.click()