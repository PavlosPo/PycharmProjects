from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element())



