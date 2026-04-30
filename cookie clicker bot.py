from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

POWER_UP_CHECK = time.monotonic() + 3
END_TIME = time.monotonic() + 300



with webdriver.Chrome() as driver:
    driver.get("https://ozh.github.io/cookieclicker/")


    choose_lang = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "langSelect-EN"))
        )
    choose_lang.click()

    cookie = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "bigCookie"))
            )
    while time.monotonic() < END_TIME:
        try:
            # Try to click the cookie normally
            cookie.click()

        except StaleElementReferenceException:
            # If the HTML refreshed and the cookie became stale,
            # instantly find the NEW version of the cookie and update the variable!
            cookie = driver.find_element(By.ID, "bigCookie")

        if time.monotonic() > POWER_UP_CHECK:
            power_ups = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
            upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")

            if power_ups:
                power_ups[-1].click()

            POWER_UP_CHECK = time.monotonic() + 10


