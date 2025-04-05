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


def test_calculator(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/'
               'slow-calculator.html')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'delay'))
    )

    delay_field = driver.find_element(By.ID, 'delay')
    delay_field.clear()
    delay_field.send_keys('45')

    button_7 = driver.find_element(
        By.CSS_SELECTOR, 'span.btn.btn-outline-primary:nth-child(1)'
    )
    button_7.click()

    button_plus = driver.find_element(
        By.CSS_SELECTOR, 'span.operator.btn.btn-outline-success'
    )
    button_plus.click()

    button_8 = driver.find_element(
        By.CSS_SELECTOR, 'span.btn.btn-outline-primary:nth-child(2)'
    )
    button_8.click()

    button_equal = driver.find_element(
        By.CSS_SELECTOR, 'span.btn.btn-outline-warning'
    )
    button_equal.click()

    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
    )

    result = driver.find_element(By.CLASS_NAME, 'screen').text
    assert result == '15', ("Результат не совпадает."
                            f" Ожидалось '15', а получено '{result}'")
