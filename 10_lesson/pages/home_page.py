from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        """
        Инициализирует главную страницу магазина.

        :param driver: Веб-драйвер Selenium
        :type driver: webdriver
        """
        self.driver = driver
        self.backpack_add_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.tshirt_add_to_cart_button = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
        self.onesie_add_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-onesie')
        self.shopping_cart_link = (By.CLASS_NAME, 'shopping_cart_link')

    def add_backpack_to_cart(self) -> None:
        """
        Добавляет рюкзак в корзину.
        """
        self.driver.find_element(*self.backpack_add_to_cart_button).click()

    def add_t_shirt_to_cart(self) -> None:
        """
        Добавляет футболку в корзину.
        """
        self.driver.find_element(*self.tshirt_add_to_cart_button).click()

    def add_onesie_to_cart(self) -> None:
        """
        Добавляет Onesie в корзину.
        """
        self.driver.find_element(*self.onesie_add_to_cart_button).click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.
        """
        self.driver.find_element(*self.shopping_cart_link).click()
