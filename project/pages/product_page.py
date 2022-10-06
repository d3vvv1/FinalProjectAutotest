from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()
        #time.sleep(10)

    def check_product_added_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        notification_product_name_added_to_basket = self.browser.find_element\
            (*ProductPageLocators.PRODUCT_NAME_ADDED_TO_BASKET)
        assert product_name.text == notification_product_name_added_to_basket.text, "Invalid product name added"

    def is_basket_price_equals_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        notification_basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert product_price.text == notification_basket_price.text, 'Basket price doesnt equal to product price'