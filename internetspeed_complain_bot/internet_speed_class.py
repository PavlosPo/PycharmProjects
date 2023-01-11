from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.down = ''
        self.up = ''


    def get_internet_speed(self):
        self.driver.get()
        self.wait_until_driver()
        pass

    def tweet_at_provider(self):
        pass

    def wait_until_driver(self, by_method: By, value: str) -> WebDriverWait:
        """ Input the "By.X" and "value" values to return a WebDriverWait element
        of timeout 10 seconds """
        return WebDriverWait(self.driver, timeout=10).until(lambda driver: self.driver.find_element(by=by_method, value=value))