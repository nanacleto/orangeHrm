from selenium import webdriver
from homePagePageObjects import LoginPage

class Login:

    def __init__(self,driver):
        self = driver
        pass

    def login(self,driver,username, passowrd):
        driver.set_login_item('txtUsername', username)
        driver.set_login_item('txtPassword', passowrd)
        driver.click_login_submit('Submit')


