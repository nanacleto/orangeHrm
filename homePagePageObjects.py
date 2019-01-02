from page_objects import PageObject, PageElement
from selenium import webdriver
from homePageLocators import *

class LoginPage(PageObject):
    #username = PageElement(id_='txtUsername')
    #password = PageElement(id_='txtPassword')
    #login = PageElement(id_='btnLogin')

    def set_login_item(self,item,text):
        self.w.find_element_by_xpath(get_login_item(item)).send_keys(text)

    def click_login_submit(self, item):
        self.w.find_element_by_xpath(get_login_item(item)).click()
