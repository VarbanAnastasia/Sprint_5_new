from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestExit:
    def test_exit(self, login_fixture, driver):
        driver = login_fixture
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)).click() # кликаем на кнопку "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.EXIT_BUTTON)).click() # ожидает и кликает на кнопку выхода
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SUBMIT_BUTTON_FOR_ENTRANCE))
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        current_url = driver.current_url
        expected_url = 'https://stellarburgers.nomoreparties.site/login'
        assert current_url == expected_url
