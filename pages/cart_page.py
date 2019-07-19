from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_be_empty_basket_text(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_BASKET_TEXT), "There are no empty basket text!"
        
    def should_be_no_basket_items(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS), "Basket items are presented, but should not be"
