from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators(object):
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

class LoginPageLocators(object):
    LOGIN_NAVBAR_LINK = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    URL_SUBSTRING = "login"
    REGISTER_FORM_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_FORM_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTER_FORM_PASSWORD_INPUT_CONFIRM = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
class ProductPageLocators(object):
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE_TAG = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    BASKET_ADDING_MESSAGE_TAG = (By.CSS_SELECTOR, "div.alertinner > strong")
    BASKET_PRICE_MESSAGE_TAG = (By.CSS_SELECTOR, "div.alertinner > p > strong")



