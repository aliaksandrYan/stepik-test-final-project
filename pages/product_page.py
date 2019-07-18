from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_adding_button()
        add = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add.click()
        self.solve_quiz_and_get_code()
        self.should_be_product_name()
        self.should_be_product_price()
        print("Product name is " + self.name)
        print("Product price is " + self.price)
        self.should_be_adding_to_basket_message()
        self.should_be_price_of_basket_message()


    def should_be_adding_button(self):
    	assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "There are no adding button!"

    def should_be_product_name(self):
    	assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name not found!"
    	self.name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_TAG), "Product price not found!"
        self.price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_TAG).text
    def should_be_adding_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ADDING_MESSAGE_TAG), "There are no 'added to basket' message!"
        assert self.name == self.browser.find_element(*ProductPageLocators.BASKET_ADDING_MESSAGE_TAG).text, "Product names don't match!"
    def should_be_price_of_basket_message(self):
    	assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE_TAG), "There are no total price of basket!"
    	assert self.price == self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE_TAG).text, "Product prices don't match!"
