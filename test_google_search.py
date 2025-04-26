from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup ChromeDriver using Service
service = Service(executable_path=r"C:\Users\malla\Desktop\selenium project\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Search
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds
time.sleep(3)

# Close browser
driver.quit()
