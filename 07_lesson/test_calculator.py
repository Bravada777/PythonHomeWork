import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.delay_field import DelayField
from pages.calculator_page import CalculatorPage


@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get('https://bonigarcia.dev/'
               'selenium-webdriver-java/slow-calculator.html')

    delay_field = DelayField(driver)
    delay_field.set_delay('45')

    calculator_page = CalculatorPage(driver)
    calculator_page.enter_number(7)
    calculator_page.press_operator('+')
    calculator_page.enter_number(8)
    calculator_page.press_operator('=')

    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element(calculator_page.screen, '15'))

    result = calculator_page.get_result()
    assert result == '15', f"Ожидалось '15', а получено '{result}'"
