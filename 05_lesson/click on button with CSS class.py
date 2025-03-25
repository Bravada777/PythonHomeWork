from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://uitestingplayground.com/classattr'
driver = webdriver.Chrome()
driver.get(url)

buttons = driver.find_elements(By.CSS_SELECTOR, 'button.btn-test')

for button in buttons:
    background_color = button.value_of_css_property('background-color')
    if background_color == 'rgba(0, 123, 255, 1)' or \
       background_color == '#007bff':
        button.click()
        break

time.sleep(2)
driver.quit()
