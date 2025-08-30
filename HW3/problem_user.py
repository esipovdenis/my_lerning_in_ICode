from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

time.sleep(1)
username = driver.find_element(By.ID, "user-name")
username.send_keys("problem_user")
time.sleep(1)
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")
time.sleep(1)
login_btn = driver.find_element(By.CSS_SELECTOR, "input#login-button")
login_btn.click()

time.sleep(5)
driver.quit()



