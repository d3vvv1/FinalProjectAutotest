from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_INPUT_EMAIL = (By.NAME, 'login-username')
    LOGIN_INPUT_PASSWORD = (By.NAME, 'login-password')
    LOGIN_SUBMIT = (By.NAME, 'login_submit')
    REGISTRATION_INPUT_EMAIL = (By.NAME, 'registration-email')
    REGISTRATION_INPUT_PASSWORD_1 = (By.NAME, 'registration-password1')
    REGISTRATION_INPUT_PASSWORD_2 = (By.NAME, 'registration-password2')
    REGISTRATION_SUBMIT = (By.NAME, 'registration_submit')