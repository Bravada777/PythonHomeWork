from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.zip_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.total_cost_label = (By.CLASS_NAME, 'summary_total_label')

    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        )
        first_name_field.send_keys(first_name)

        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        )
        last_name_field.send_keys(last_name)

        zip_code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.zip_code_input)
        )
        zip_code_field.send_keys(postal_code)

        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        )
        continue_btn.click()

    def get_total_cost(self) -> str:
        total_cost_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_cost_label)
        )
        total_cost = total_cost_element.text
        total_cost = total_cost.replace('Total:', '').strip()
        return total_cost
