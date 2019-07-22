from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self,email, password):
        reg_link = self.browser.find_element(*LoginPageLocators.LOGIN_NAVBAR_LINK)
        reg_link.click()
        
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_INPUT)
        email_input.send_keys(email)
        
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT)
        password_input.send_keys(password)
        
        password_input_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT_CONFIRM)
        password_input_confirm.send_keys(password)

        submit_form_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        submit_form_button.click()


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
    