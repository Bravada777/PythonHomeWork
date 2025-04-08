from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_add_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.t_shirt_add_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        self.onesie_add_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-onesie')
        self.cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def add_backpack_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.backpack_add_to_cart_button)
        ).click()

    def add_t_shirt_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.t_shirt_add_to_cart_button)
        ).click()

    def add_onesie_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.onesie_add_to_cart_button)
        ).click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()
