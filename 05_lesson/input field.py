from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

service = Service(
    r'C:\Users\Admin\Desktop\Питон\PythonHomeWork\05_lesson\geckodriver.exe'
)
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options, service=service)

url = 'http://the-internet.herokuapp.com/inputs'
driver.get(url)

input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_field.send_keys('1000')
time.sleep(2)
input_field.clear()
time.sleep(2)
input_field.send_keys('999')

time.sleep(2)
driver.quit()
