from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
wait = WebDriverWait(driver, 40, 0.1)

status = wait.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, "#text"), 'Done!'))
attribute = driver.find_element(
    By.CSS_SELECTOR, "#award").get_attribute('src')
print(attribute)
