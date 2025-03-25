from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def open_page_and_click_blue_button():
    url = 'http://uitestingplayground.com/dynamicid'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    blue_button = driver.find_element(
        By.XPATH, '//button[contains(text(), "Button")]'
    )
    blue_button.click()
    time.sleep(2)
    driver.quit()


open_page_and_click_blue_button()
