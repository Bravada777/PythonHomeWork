import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope='module')
def driver():
    options = Options()
    # Добавление аргумента для запуска в режиме инкогнито, потому что не давало всплывающее окно дальше отработать коду
    options.add_argument("--incognito")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@allure.feature('Покупка товаров')
@allure.story('Тестирование процесса покупки')
def test_purchase(driver):
    with allure.step('Открытие страницы'):
        driver.get('https://www.saucedemo.com/')

    with allure.step('Авторизация'):
        login_page = LoginPage(driver)
        login_page.enter_username('standard_user')
        login_page.enter_password('secret_sauce')
        login_page.click_login_button()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'inventory_container'))
        )

    with allure.step('Главная страница магазина'):
        home_page = HomePage(driver)
        home_page.add_backpack_to_cart()
        home_page.add_t_shirt_to_cart()
        home_page.add_onesie_to_cart()
        home_page.go_to_cart()

    with allure.step('Страница корзины'):
        cart_page = CartPage(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'checkout'))
        )
        cart_page.click_checkout_button()

    with allure.step('Страница оформления заказа'):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form('Дарья', 'Кондрашова', '125239')

    with allure.step('Проверка итоговой суммы'):
        total_cost = checkout_page.get_total_cost()
        expected_cost = '$58.29'
        assert total_cost == expected_cost, (
            f'Ожидаемая стоимость {expected_cost}, фактическая стоимость {total_cost}')
