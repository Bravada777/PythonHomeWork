from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.buttons = {
            '7': (By.CSS_SELECTOR, 'span.btn.btn-outline-primary:nth-child(1)'),
            '8': (By.CSS_SELECTOR, 'span.btn.btn-outline-primary:nth-child(2)'),
            '+': (By.CSS_SELECTOR, 'span.operator.btn.btn-outline-success'),
            '=': (By.CSS_SELECTOR, 'span.btn.btn-outline-warning'),
        }
        self.screen = (By.CLASS_NAME, 'screen')

    def enter_number(self, number):
        locator = self.buttons[str(number)]
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def press_operator(self, operator):
        locator = self.buttons[operator]
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def get_result(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.screen)
        ).text
