from .base_page import BasePage
from .locators import LoginPageLocators
import time

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

    def register_new_email(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_PASSWORD_1)
        password_input.send_keys(password)
        password_input_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_PASSWORD_2)
        password_input_confirm.send_keys(password)
        registration_submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_submit_button.click()

