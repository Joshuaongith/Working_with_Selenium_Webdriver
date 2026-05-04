from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time



with webdriver.Chrome() as driver:
    driver.get("https://ozh.github.io/cookieclicker/")

    # Wait for and click the English language button
    choose_lang = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN"))
    )
    choose_lang.click()

    # Wait for the game to fully load and locate the Big Cookie
    cookie = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )

    # Start timers ONLY after the game is completely ready
    timeout = time.monotonic() + 5
    end_time = time.monotonic() + 300  # 5-minute total run time

    # Main game loop
    while time.monotonic() < end_time:

        # 1. Click the cookie (with instant Stale Element recovery)
        try:
            cookie.click()
        except StaleElementReferenceException:
            cookie = driver.find_element(By.ID, "bigCookie")
            cookie.click()

            # 2. Check the store every 5 seconds
        if time.monotonic() > timeout:

            # Find all currently affordable items
            power_ups = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

            if power_ups:
                try:
                    # Buy the most expensive available item
                    power_ups[-1].click()
                except StaleElementReferenceException:
                    # Ignore if the store refreshes exactly as we click
                    pass

                    # Reset the store check timer
            timeout = time.monotonic() + 5

    # 3. Game over - Read the final score safely
    for _ in range(5):
        try:
            cps = driver.find_element(By.ID, "cookiesPerSecond").text
            print(f"Final Score: {cps}")
            break  # Success! Break the loop.

        except StaleElementReferenceException:
            time.sleep(0.1)

    else:
        # Only triggers if it failed 5 times in a row
        print("Bot failed to grab the final score due to game refresh.")