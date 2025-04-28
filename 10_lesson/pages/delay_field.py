from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DelayField:
    def __init__(self, driver):
        """
        Инициализирует поле задержки.

        :param driver: Веб-драйвер Selenium
        :type driver: webdriver
        """
        self.driver = driver
        self.delay_input = (By.ID, 'delay')

    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает задержку.

        :param seconds: Количество секунд задержки
        :type seconds: str
        """
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.delay_input)
        )

        input_field.clear()
        input_field.send_keys(seconds)
