from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get('http://myawesomebtre.herokuapp.com/')
print(driver.title)
search = driver.find_element_by_name('keywords')
search.send_keys('pool')
search.send_keys(Keys.RETURN)
try:
    listings = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "listings"))
    )
except:
    driver.quit()
print(listings.text)
driver.quit()

# articles = listings.find_element_by_class_name("col-md-6 col-lg-4 mb-4")
#     for article in articles:
#         price = article.find_element_by_class_name(
#             "badge badge-secondary text-white")
#         print(price.text)
