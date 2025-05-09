from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

URL = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)


def buy():
    try:
        div_elements = driver.find_elements(By.XPATH, "//div[@id='store']//div[not(@class) or @class='']")
        if div_elements:
            div_elements[-1].click()
    except Exception as e:
        pass


start_time = time.time()
timeout = 5 * 60
buy_time = time.time() + 5

cookie = driver.find_element(By.ID, "cookie")

while time.time() - start_time < timeout:
    cookie.click()

    if time.time() > buy_time:
        buy()
        buy_time = time.time() + 5  # schedule next buy in 5 seconds

# When the timeout finishes
score = driver.find_element(By.ID, "cps")
print(f"Final score: {score.text}")
