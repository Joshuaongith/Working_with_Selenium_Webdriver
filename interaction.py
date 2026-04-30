from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
# article_count.click()

# find element by link text
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# find the "Search" <input> by Name
# select the search bar
search = driver.find_element(By.NAME,"search")

# send keyboard input to selenium
search.send_keys("Python", Keys.ENTER)
