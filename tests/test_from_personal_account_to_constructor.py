from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestPersonalAccountToConstructor:
    def test_from_personal_to_constructor(self, login_fixture, driver):
        driver = login_fixture
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUILDER_BUTTON)).click() #ожидает и кликает на конструктор
        current_url = driver.current_url
        expected_url = 'https://stellarburgers.nomoreparties.site/'
        assert current_url == expected_url

    def test_from_personal_to_logo(self, login_fixture, driver):
        driver = login_fixture
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)).click() # ожидает и переходит в личный кабинет
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO_BUTTON)).click() # ожидаем и переходит на логотип
        current_url = driver.current_url
        expected_url = 'https://stellarburgers.nomoreparties.site/'
        assert current_url == expected_url



