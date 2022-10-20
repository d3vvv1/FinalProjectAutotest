from .base_page import BasePage
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

LANGUAGES = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}


class BasketPage(BasePage):
    def is_basket_empty_label_presented(self):
        try:
            language = self.browser.execute_script(
                "return window.navigator.userLanguage || window.navigator.language")
            label = self.browser.find_element(*BasePageLocators.EMPTY_BASKET_LABEL)
            if not LANGUAGES[language] in label:
                return False
        except NoSuchElementException:
            return False
        return True

    def is_no_elements_in_basket(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(*BasePageLocators.BASKET_ITEMS))
        except TimeoutException:
            return True
        return False
