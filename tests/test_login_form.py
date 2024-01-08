from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from constants import Constants


class TestLogin:
    # вход по кнопке «Войти в аккаунт» на главной)
    def test_login_main_page(self, driver, login_fixture):
        driver = login_fixture
        assert driver.find_element(*Locators.ORDER_FORMATION).is_displayed()  # проверка наличия кнопки "Оформить заказ"

    def test_login_personal_account(self, driver):
        # вход через кнопку «Личный кабинет»,
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                Locators.PERSONAL_ACCOUNT)).click()  # кликаем на кнопку личного кабинета на главном экране

        driver.find_element(*Locators.EMAIL_FIELD).send_keys(*Constants.TEST_EMAIL)  # вводим email для входа
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(*Constants.TEST_PASSWORD)  # вводим пароль для входа
        driver.find_element(*Locators.SUBMIT_BUTTON_FOR_ENTRANCE).click()  # кликаем на кнопку входа
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            Locators.ORDER_FORMATION))  # ждем пока появится кнопка "Оформить заказ" на главном экране
        assert driver.find_element(*Locators.ORDER_FORMATION).is_displayed()  # проверка наличия кнопки "Оформить заказ"

    def test_login_registration_form(self, driver):
        # вход через форму регистрации
        driver.find_element(*Locators.LOG_IN_BUTTON).click()  # кликаем на кнопку входа на главном экране
        driver.find_element(
            *Locators.REGISTRATION).click()  # кликаем на кнопку регистрации после перехода из главного экрана
        driver.find_element(*Locators.LOG_IN_BUTTON_IN_REG_FORM).click()  # кликаем на кнопку входа в форме регистрации
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(*Constants.TEST_EMAIL)  # вводим email для входа
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(*Constants.TEST_PASSWORD)  # вводим пароль для входа
        driver.find_element(*Locators.SUBMIT_BUTTON_FOR_ENTRANCE).click()  # кликаем на кнопку входа
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.EMAIL_FIELD))  # ждем пока появится кнопка email для входа
        assert driver.find_element(
            *Locators.PERSONAL_ACCOUNT).is_displayed()  # проверка наличия личного кабинета на главном экране

    def test_login_through_password_recovery(self, driver):
        # вход через кнопку в форме восстановления пароля.
        driver.find_element(*Locators.LOG_IN_BUTTON).click()  # кликаем на кнопку входа на главном экране
        driver.find_element(
            *Locators.PASSWORD_RECOVERY_BUTTON).click()  # кликаем на кнопку восстановления пароля после перехода из главного экрана
        driver.find_element(
            *Locators.LOG_IN_BUTTON_IN_REG_FORM).click()  # кликаем на кнопку входа в форме восстановления пароля
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(*Constants.TEST_EMAIL)  # вводим email для входа
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(*Constants.TEST_PASSWORD)  # вводим пароль для входа
        driver.find_element(*Locators.SUBMIT_BUTTON_FOR_ENTRANCE).click()  # кликаем на кнопку входа
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.EMAIL_FIELD))  # ждем пока появится кнопка email для входа
        assert driver.find_element(
            *Locators.PERSONAL_ACCOUNT).is_displayed()  # проверка наличия личного кабинета на главном экране
