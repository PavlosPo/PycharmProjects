from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://tinder.com")
time.sleep(3)
login_in_button = driver.find_elements(by=By.CSS_SELECTOR, value='.w1u9t036 .l17p5q9z')[2]
login_in_button.click()

facebook_login = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element(by=By.XPATH, value='//*[@id="o793001744"]/main/div/div[1]/div/div/div[3]/span'))

# print([item.text for item in facebook_login])
# print(len(facebook_login))
# dummy_elements[0].click()
print(facebook_login.text)
time.sleep(3)