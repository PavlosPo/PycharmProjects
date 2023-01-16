from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def WebDriverWait(self, by_method: By, value: str, timeout=10) -> WebDriverWait:
        item = WebDriverWait(self.driver, timeout=timeout).until(lambda driver: self.driver.find_element(by=by_method, value=value))
        return item

    def WebDriverWaits(self, by_method: By, value: str, timeout=10) -> WebDriverWait:
        items = WebDriverWait(self.driver, timeout=timeout).until(lambda driver: self.driver.find_elements(by=by_method, value=value))
        return items

    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(1)
        # Accept Cookies
        cookies = self.WebDriverWait(by_method=By.XPATH,
                                           value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        cookies.click()
        # Insert Udername and password
        time.sleep(1)
        input_username = self.driver.find_elements(by=By.TAG_NAME, value="input")[0]
        input_password = self.driver.find_elements(by=By.TAG_NAME, value="input")[1]
        input_username.send_keys(username)
        input_password.send_keys(password)
        # Click login
        time.sleep(2)
        login_button = self.WebDriverWait(by_method=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        # Turn off notifications dialog
        time.sleep(2)
        self.driver.get("https://www.instagram.com")  # Refresh, otherwise not working
        print("Refreshed")
        time.sleep(1)
        notification_button_off = self.WebDriverWaits(by_method=By.TAG_NAME, value='button')[-1]
        print("Found the button Notification")
        notification_button_off.click()
        print("Clicked the notification off")
        time.sleep(5)


    def find_followers(self):
        self.driver.get("https://www.instagram.com/wildcamping_gr/")
        first_follow_button = self.WebDriverWait(by_method=By.TAG_NAME, value="button")
        first_follow_button.click()
        print('Pressed the follow button')
        time.sleep(100)


bot = InstaFollower()
bot.login()
bot.find_followers()

