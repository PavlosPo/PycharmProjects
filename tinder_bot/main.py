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


# Phone Number Section
phone_number_login = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element(by=By.XPATH, value='//*[@id="o793001744"]/main/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]'))
phone_number_login.click()
type_phone_number = WebDriverWait(driver, timeout=10).until(lambda driver: driver.find_element(by=By.NAME, value="phone_number"))
type_phone_number.send_keys("###########")
complete_phone_number_button = WebDriverWait(driver, timeout=600).until(lambda driver: driver.find_element(by=By.XPATH, value='//*[@id="o793001744"]/main/div/div[1]/div/button/div[2]'))
complete_phone_number_button.click()

like_button = WebDriverWait(driver, timeout=10).until(lambda driver: driver.find_element(by=By.XPATH, value='//*[@id="o-1773584476"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button/span/span'))
like_button.click()
time.sleep(3)
print("Clicked")