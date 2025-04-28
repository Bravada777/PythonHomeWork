import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.delay_field import DelayField
from pages.calculator_page import CalculatorPage
import allure


# Фикстура драйвера остается прежней
@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@allure.title("Проверка работы калькулятора")
@allure.description("Тестирует работу онлайн-калькулятора с использованием Selenium.")
def test_calculator(driver):
    # Начинаем шаги тестирования
    with allure.step("Открытие страницы"):
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    with allure.step("Установка задержки расчета"):
        delay_field = DelayField(driver)
        delay_field.set_delay('45')

    with allure.step("Ввод чисел и выполнение операций"):
        calculator_page = CalculatorPage(driver)
        calculator_page.enter_number(7)
        calculator_page.press_operator('+')
        calculator_page.enter_number(8)
        calculator_page.press_operator('=')

    with allure.step("Ожидание появления результата"):
        WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element(calculator_page.screen, '15'))

    with allure.step("Получение результата"):
        result = calculator_page.get_result()
        assert result == '15', f"Ожидалось '15', а получено '{result}'"
