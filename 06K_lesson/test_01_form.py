from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_fill_form(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/'
               'data-types.html')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'first-name'))
    )

    first_name_field = driver.find_element(By.NAME, 'first-name')
    last_name_field = driver.find_element(By.NAME, 'last-name')
    address_field = driver.find_element(By.NAME, 'address')
    email_field = driver.find_element(By.NAME, 'e-mail')
    phone_number_field = driver.find_element(By.NAME, 'phone')
    city_field = driver.find_element(By.NAME, 'city')
    country_field = driver.find_element(By.NAME, 'country')
    job_position_field = driver.find_element(By.NAME, 'job-position')
    company_field = driver.find_element(By.NAME, 'company')

    first_name_field.send_keys('Иван')
    last_name_field.send_keys('Петров')
    address_field.send_keys('Ленина, 55-3')
    email_field.send_keys('test@skypro.com')
    phone_number_field.send_keys('+7985899998787')
    city_field.send_keys('Москва')
    country_field.send_keys('Россия')
    job_position_field.send_keys('QA')
    company_field.send_keys('SkyPro')

    submit_button = driver.find_element(
        By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3'
    )
    submit_button.click()

    WebDriverWait(driver, 10).until_not(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3'
        ))
    )
