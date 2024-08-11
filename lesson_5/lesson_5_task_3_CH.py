from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/classattr')

button = driver.find_element(
        By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
button.click()
driver.switch_to.alert.accept()

count = 0

for x in range(3):
    button = driver.find_element(
        By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    button.click()
    driver.switch_to.alert.accept()
    count = count + 1
    print(count)
