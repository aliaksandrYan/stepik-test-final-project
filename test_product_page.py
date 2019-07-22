import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
import time

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.login_user
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        self.browser = browser
        self.default_link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(self.browser, self.default_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email,"superpass123")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    @pytest.mark.parametrize('link', links)
    def test_user_can_add_product_to_cart(self,browser,link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_cart(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_basket_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_basket_text()
    cart_page.should_be_no_basket_items()