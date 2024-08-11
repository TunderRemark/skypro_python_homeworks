from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/login')

username = driver.find_element(By.ID, "username")
username.click()
username.send_keys("tomsmith")
sleep(1)
password = driver.find_element(By.ID, "password")
password.click()
password.send_keys("SuperSecretPassword!")
sleep(2)
button = driver.find_element(By.TAG_NAME, "button").click()
sleep(2)
driver.quit()
