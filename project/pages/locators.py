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

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    #BASKET_PRICE = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/text()')
    BUTTON_OPEN_BASKET = (By.CSS_SELECTOR, '.btn-default')
    PRODUCT_NAME_ADDED_TO_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
