# import selenium
# from login import LoginPage
#
# driver = selenium.webdriver.Chrome()
# driver.get('https://opensource-demo.orangehrmlive.com/')
#
# page = LoginPage(driver)
# page.username('Admin')
# page.password('admin123')
#
# driver.find_element_by_id(page.username).send_keys()
#
# #page.clickLogin.click()

from login import Login
from selenium import webdriver
from homePagePageObjects import LoginPage





driver = webdriver.Chrome()
page = LoginPage(driver)
page.get("https://opensource-demo.orangehrmlive.com/")

l = Login(driver)
l.login(page,'Admin','admin123')
