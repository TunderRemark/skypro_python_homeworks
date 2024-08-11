from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput ')

field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
field.send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
new_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(new_button)
driver.quit()
