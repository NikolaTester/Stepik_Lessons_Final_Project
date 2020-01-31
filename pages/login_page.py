from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    #def should_be_login_link(self):
    #    assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_url(self):
        #проверка на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "Current url hasn't the substring"

    def should_be_login_form(self):
        #проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_PAGE), "Login link is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_PAGE), "Login link is not presented"
