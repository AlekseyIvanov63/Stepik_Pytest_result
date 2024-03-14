from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес
        text = '?promo=newYear'
        url = self.browser.current_url
        assert text in url, 'No URL'

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Button add to basket is not presented"
