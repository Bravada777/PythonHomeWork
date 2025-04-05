from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_purchase(driver):
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.ID, 'user-name')
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_field.send_keys('standard_user')
    password_field.send_keys('secret_sauce')
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, '.inventory_item_name'))
    )

    backpack_add_to_cart_button = driver.find_element(
        By.ID, 'add-to-cart-sauce-labs-backpack'
    )
    backpack_add_to_cart_button.click()

    t_shirt_add_to_cart_button = driver.find_element(
        By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'
    )
    t_shirt_add_to_cart_button.click()

    onesie_add_to_cart_button = driver.find_element(
        By.ID, 'add-to-cart-sauce-labs-onesie'
    )
    onesie_add_to_cart_button.click()

    cart_link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_link.click()

    checkout_button = driver.find_element(By.ID, 'checkout')
    checkout_button.click()

    first_name_field = driver.find_element(By.ID, 'first-name')
    last_name_field = driver.find_element(By.ID, 'last-name')
    zip_code_field = driver.find_element(By.ID, 'postal-code')

    first_name_field.send_keys('Дарья')
    last_name_field.send_keys('Кондрашова')
    zip_code_field.send_keys('125239')

    continue_button = driver.find_element(By.ID, 'continue')
    continue_button.click()

    total_cost = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    total_cost = total_cost.replace('Total:', '').strip()
    expected_cost = '$58.29'
    assert total_cost == expected_cost, (
        f'Ожидаемая стоимость {expected_cost}, '
        f'фактическая стоимость {total_cost}'
    )
