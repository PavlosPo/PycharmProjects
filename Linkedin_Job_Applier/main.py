from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import datetime, time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.linkedin.com/home")


def login_in(driver=driver):
    time.sleep(1)
    email = driver.find_element(by=By.ID, value="session_key")
    password = driver.find_element(by=By.ID, value="session_password")
    sign_in = driver.find_element(by=By.CLASS_NAME, value="sign-in-form").find_element(by=By.CLASS_NAME,
                                                                                       value="sign-in-form__submit-button")
    sign_in.click()


def go_jobs_page(driver=driver):
    time.sleep(1)
    driver.get(
        "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


def apply_to_jobs():
    def find_jobs():
        """Returns the Job postings as a list of li item tags from html"""
        job_postings = driver.find_element(by=By.CLASS_NAME, value="scaffold-layout__list-container")
        jobs = job_postings.find_elements(by=By.CSS_SELECTOR, value="li .artdeco-entity-lockup__title")
        print(f"Found: {len(jobs)} Job Postings.")
        return jobs

    def click_and_fill_jobs():
        driver.implicitly_wait(3)
        # Finds the telephone field
        telephone = driver.find_element(by=By.CLASS_NAME, value='artdeco-text-input--input')
        telephone.send_keys("6940820115")

    jobs = find_jobs()
    for index, job in enumerate(jobs):
        time.sleep(1.5)

        # Apply Button
        easy_apply = job.find_element(by=By.CLASS_NAME, value='jobs-apply-button')
        print("Found the Button")
        easy_apply.click()
        print("Pressed the Button")

        click_and_fill_jobs()



login_in()
go_jobs_page()
apply_to_jobs()
