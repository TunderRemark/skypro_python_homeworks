from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/ajax')
wait = WebDriverWait(driver, 20, 0.1)

button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

result = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, ".bg-success"))).text
print(result)
driver.quit()
