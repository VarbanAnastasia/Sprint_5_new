
from random import randint

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from faker import Faker


def generate_login_email():
    fake = Faker()
    return fake.email()


def generate_password():
    password = randint(100000, 999999)
    return password


class TestRegistration:

    def test_registration(self, driver):
        name = "Anastasia"
        email = generate_login_email()
        password = generate_password()
        driver.find_element(*Locators.LOG_IN_BUTTON).click()  # кликаем на кнопку входа на главном экране
        driver.find_element(
            *Locators.REGISTRATION).click()  # кликаем на кнопку регистрации после перехода из главного экрана
        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys(name)  # вводим имя в форме регистрации
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)  # вводим email в форме регистрации
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)  # вводим пароль в форме регистрации
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()  # кликаем на кнопку регистрации в форме регистрации
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.EMAIL_FIELD))  # ждем пока появится кнопка email для входа
        print(email)
        print(password)
        assert driver.find_element(
            *Locators.PERSONAL_ACCOUNT).is_displayed()  # проверка наличия личного кабинета на главном экране

    def test_incorrect_password_message(self, driver):
        name = "Anastasia1233234"
        email = generate_login_email()
        password = "123"

        driver.find_element(*Locators.LOG_IN_BUTTON).click()  # кликаем на кнопку входа на главном экране
        driver.find_element(
            *Locators.REGISTRATION).click()  # кликаем на кнопку регистрации после перехода из главного экрана
        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys(name)  # вводим имя
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)  # вводим email
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)  # вводим пароль
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()  # кликаем на кнопку регистрации
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.SUBMIT_BUTTON_FOR_ENTRANCE))  # ждем пока появится кнопка Входа
        incorrect_pass = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            Locators.INCORRECT_PASSWORD_MESSAGE)).text  # ждем пока появится сообщение об ошибке
        assert incorrect_pass == "Некорректный пароль"  # проверка наличия сообщения
