from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

price_Naira = driver.find_element(By.CLASS_NAME, "a-price-whole").text
price_kobo = driver.find_element(By.CLASS_NAME, "a-price-fraction").text


print(f"{price_Naira}.{price_kobo}")