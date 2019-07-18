from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.URL_SUBSTRING in self.browser.current_url, "URL without login substring!"
        

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There are no register form!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There are no login form!"

       