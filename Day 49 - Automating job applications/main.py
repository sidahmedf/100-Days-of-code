import os

import selenium
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

URL = "https://www.linkedin.com/login"
LOGIN = os.getenv("LOGIN")
PASSWRD = os.getenv("PASSWRD")


# Step 1: Go directly to the LinkedIn login page
driver.get(URL)

# Step 2: Find the email input and password input and send credentials
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
email_input.send_keys(LOGIN)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(PASSWRD)

# Step 3: Submit the form
password_input.send_keys(Keys.ENTER)

# Step 4: After logging in, go to the job search page
WebDriverWait(driver, 10).until(EC.url_contains("feed"))  # Wait until logged in
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4212396350&geoId=105015875&keywords=Ing%C3%A9nieur"
           "%20logiciel&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")

# Step 5: Select the job
job_cards = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container--clickable"))
)

for job in job_cards:
    try:
        time.sleep(0.5)
        job.click()

        # Wait until the "Save" button is clickable
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Save")]'))
        )
        save_button.click()

        time.sleep(0.5)

        # Try to find and click the "Follow" button if exists
        try:
            follow_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Follow")]'))
            )
            follow_button.click()
            time.sleep(0.5)
        except (NoSuchElementException, TimeoutError):
            print("No Follow button found, moving on.")

    except (StaleElementReferenceException, ElementClickInterceptedException) as e:
        print(f"Error with a job card: {e}")
        continue
