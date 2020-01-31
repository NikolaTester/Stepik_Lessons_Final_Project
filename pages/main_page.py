from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators
import time

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "Current url hasn't the substring"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_PAGE), "Login link is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_PAGE), "Login link is not presented"