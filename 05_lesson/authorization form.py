from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(
    r'C:\Users\Admin\Desktop\Питон\PythonHomeWork\05_lesson\geckodriver.exe'
)
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options, service=service)

url = 'http://the-internet.herokuapp.com/login'
driver.get(url)

username_field = driver.find_element(By.ID, 'username')
username_field.send_keys('tomsmith')

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('SuperSecretPassword!')

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//button[@type="submit"][.//i[contains(@class, "fa-sign-in")]]'
    ))
)

login_button = driver.find_element(
    By.XPATH, '//button[@type="submit"][.//i[contains(@class, "fa-sign-in")]]'
)
login_button.click()

time.sleep(2)
driver.quit()
