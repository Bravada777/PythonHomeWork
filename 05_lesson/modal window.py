from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(
    r'C:\Users\Admin\Desktop\Питон\PythonHomeWork\05_lesson\geckodriver.exe'
)
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options, service=service)

driver.get('http://the-internet.herokuapp.com/entry_ad')
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'modal-footer'))
)
close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable
    ((By.XPATH, "//div[@class='modal-footer']/p[text()='Close']"))
)
close_button.click()

driver.quit()
