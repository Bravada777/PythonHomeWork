from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """
        Инициализирует страницу входа.

        :param driver: Веб-драйвер Selenium
        :type driver: webdriver
        """
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def enter_username(self, username: str) -> None:
        """
        Ввод имени пользователя.

        :param username: Имя пользователя
        :type username: str
        """
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Ввод пароля.

        :param password: Пароль
        :type password: str
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self) -> None:
        """
        Кликает на кнопку входа.
        """
        self.driver.find_element(*self.login_button).click()
