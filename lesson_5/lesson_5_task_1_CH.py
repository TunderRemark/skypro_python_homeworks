from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

for x in range(5):
    add_button = driver.find_element(
        By.XPATH, "//button[text()='Add Element']").click()
    delete_buttons = driver.find_elements(
        By.XPATH, "//button[text()='Delete']")

print(
    f"Размер списка: {len(delete_buttons)}")
