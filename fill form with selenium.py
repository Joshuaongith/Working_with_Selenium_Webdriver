from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# selenium setup to keep tab open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# select website
driver.get("https://secure-retreat-92358.herokuapp.com/")

# find first name field
first_name = driver.find_element(By.NAME, "fName")


last_name = driver.find_element(By.NAME, "lName")


email = driver.find_element(By.NAME, "email")

first_name.send_keys("Mildest")
last_name.send_keys("Colonel")
email.send_keys("mildestcolonel@gmail.com", Keys.ENTER)

