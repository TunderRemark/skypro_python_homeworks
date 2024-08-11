from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/inputs')

field = driver.find_element(By.TAG_NAME, "input")
field.click()
field.send_keys("1000")
sleep(3)
field.clear()
sleep(3)
field.send_keys("999")
sleep(3)

driver.quit()
