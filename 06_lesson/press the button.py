from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/ajax')

button = driver.find_element(By.ID, 'ajaxButton')
button.click()

wait = WebDriverWait(driver, 16)
green_text_box = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success'))
)
loaded_text = green_text_box.text

print(loaded_text)

driver.quit()
