from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

# class MainPageLocators(object):
    
    
class LoginPageLocators(object):
    LOGIN_FORM = (By.ID,"login_form")
    REGISTER_FORM = (By.ID,"register_form")
    URL_SUBSTRING = "login"

class ProductPageLocators(object):
    ADD_BUTTON = (By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE_TAG = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    BASKET_ADDING_MESSAGE_TAG = (By.CSS_SELECTOR, "div.alertinner > strong")
    BASKET_PRICE_MESSAGE_TAG = (By.CSS_SELECTOR, "div.alertinner > p > strong")