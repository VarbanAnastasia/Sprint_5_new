import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from locators import Locators
from constants import Constants
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def login_fixture(driver):
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Locators.LOG_IN_BUTTON)).click()  # кликаем на кнопку входа на главном экране
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(*Constants.TEST_EMAIL)  # вводим email для входа
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(*Constants.TEST_PASSWORD)  # вводим пароль для входа
    driver.find_element(*Locators.SUBMIT_BUTTON_FOR_ENTRANCE).click()  # кликаем на кнопку входа
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        Locators.ORDER_FORMATION))  # ждем пока появится кнопка "Оформить заказ" на главном экране
    return driver
