
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_purchase(driver):
    driver.get('https://www.saucedemo.com/')

    # Авторизация
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()

    # Главная страница магазина
    home_page = HomePage(driver)
    home_page.add_backpack_to_cart()
    home_page.add_t_shirt_to_cart()
    home_page.add_onesie_to_cart()
    home_page.go_to_cart()

    # Страница корзины
    cart_page = CartPage(driver)
    cart_page.click_checkout_button()

    # Страница оформления заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form('Дарья', 'Кондрашова', '125239')

    # Проверка итоговой суммы
    total_cost = checkout_page.get_total_cost()
    expected_cost = '$58.29'
    assert total_cost == expected_cost, (
        f'Ожидаемая стоимость {expected_cost}, фактическая стоимость {total_cost}')
