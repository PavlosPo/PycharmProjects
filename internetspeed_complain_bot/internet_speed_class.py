import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.results_link = ''
        self.down = ''
        self.up = ''

    def get_internet_speed(self):
        internet_speed_site = self.driver.get("https://www.speedtest.net")
        time.sleep(1)
        # Accept the terms
        self.driver.find_element(by=By.ID, value="onetrust-accept-btn-handler").click()
        # Find the start button to tart the test
        start_button = self.wait_until_driver(By.XPATH,
                                              value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button[0].click()
        # Wait for results
        results = self.wait_until_driver(By.CLASS_NAME, value='social-icon', timeout=100)
        result_link = results[0].get_attribute('href')  # it is the first anchertag on the HTML

        # Go to results page
        try:
            # Save results in the class
            self.results_link = result_link
            self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/span').text
            self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/span').text
            time.sleep(2)
        except:
            print("Error on getting the link")
            pass


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        # TODO: Tweet about the speed that you got from the test
        pass

    def wait_until_driver(self, by_method: By, value: str, timeout=10) -> [WebDriverWait]:
        """ Input the "By.X" and "value" values to return a WebDriverWait element
        of timeout 10 seconds """
        return WebDriverWait(self.driver, timeout=timeout).until(
            lambda driver: self.driver.find_elements(by=by_method, value=value))


InternetSpeedTwitterBot().get_internet_speed()
