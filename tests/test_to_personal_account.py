from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestPersonalAccount:
    def test_to_personal_account(self, login_fixture, driver):
        driver = login_fixture
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)).click()
        current_url = driver.current_url
        expected_url = 'https://stellarburgers.nomoreparties.site/account'
        assert current_url == expected_url


