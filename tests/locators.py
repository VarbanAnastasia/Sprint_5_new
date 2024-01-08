from selenium.webdriver.common.by import By


class Locators:
    LOG_IN_BUTTON = (By.XPATH,
                     "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                     "button_button_size_large__G21Vg']")  # кнопка входа на главном экране
    REGISTRATION = (By.XPATH,
                    "//a[@class='Auth_link__1fOlj' and @href='/register']")  # кнопка регистрации после перехода из главного экрана
    REGISTRATION_BUTTON = (By.XPATH, ".//*[text()='Зарегистрироваться']")  # кнопку регистрации в форме регистрации
    SUBMIT_BUTTON_FOR_ENTRANCE = (By.XPATH,
                                  "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                  "button_button_size_medium__3zxIa']")  # Кнопка "Войти" в форме входа
    LOG_IN_BUTTON_IN_REG_FORM = (
    By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']")  # Кнопка "Войти" в форме регистрации
    PASSWORD_RECOVERY_BUTTON = (
    By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']")  # Кнопка "Войти" в форме регистрации

    NAME_INPUT_FIELD = (
    By.XPATH, "//label[text()='Имя']/following-sibling::*")  # Поле ввода имени пользователя в регистрации
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # Поле ввода e-mail в регистрации
    PASSWORD_INPUT_FIELD = (By.XPATH, ".//*[@name='Пароль']")  # Поле ввода пароля в регистрации
    INCORRECT_PASSWORD_MESSAGE = (By.XPATH,
                                  "//p[@class='input__error text_type_main-default']")  # сообщение об ошибке при некорректном пароле в форме регистрации

    EMAIL_FIELD = (By.XPATH,
                   "//input[@class='text input__textfield text_type_main-default' and @type='text']")  # Поле ввода e-mail в форме Вход
    PASSWORD_FIELD = (By.XPATH,
                      '//input[@class="text input__textfield text_type_main-default" and @type="password"]')  # Поле ввода пароля в форме Вход

    ORDER_FORMATION = (By.XPATH,
                       "//div[@class='BurgerConstructor_basket__container__2fUl3 mt-10']/button")  # кнопка "Оформить заказ" на главном экране
    PERSONAL_ACCOUNT = (By.XPATH,
                        '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]')  # кнопка личного кабинета на главном экране
    BUILDER_BUTTON = (By.XPATH,
                      "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")  # кнопка "Конструктор" на главном экране
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # кнопка "Логотип" на главном экране
    EXIT_BUTTON = (By.XPATH,
                   "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")  # кнопка "Выход" в личном кабинете

    SAUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']/parent::*")  # кнопка "Соусы"
    BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']/parent::*")  # кнопка"Булки"
    TOPPINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']/parent::*")  # кнопка"Начинки"
