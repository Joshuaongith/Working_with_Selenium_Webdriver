from selenium import webdriver
from selenium.webdriver.common.by import By

# initialize selenium web driver
with webdriver.Chrome() as driver:
    # select website to scrape from
    driver.get("https://www.python.org/")

    # Grab the HTML container for every single event in the list
    events_data = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')

    # DATA PARSING
    events = {}
    for i, event in enumerate(events_data):
        events[i] = {
            # Grab the hidden datetime attribute and slice off the timezone info
            "time": event.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0],

            # Grab the visible text of the event link
            "title": event.find_element(By.TAG_NAME, "a").text
        }
    print(events)

    # using the with keyword the session closes automatically