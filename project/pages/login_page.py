from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_EMAIL), 'Login email input is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_PASSWORD), 'Login password input is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), 'Login submit button is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_INPUT_EMAIL),\
            'Registration email input is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_INPUT_PASSWORD_1),\
            'Registration password input is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_INPUT_PASSWORD_2), \
            'Registration second password input is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), \
            'Registration submit button is not presented'
