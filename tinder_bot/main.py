from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://tinder.com")
time.sleep(3)
login_in_button = driver.find_elements(by=By.CSS_SELECTOR, value='.w1u9t036 .l17p5q9z')[2]
login_in_button.click()
time.sleep(3)


