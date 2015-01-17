#coding:utf-8

from BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    firstPostLinkLocator = (By.CSS_SELECTOR,'h1.entry-title a')

    def __init__(self,driver):
        super(HomePage,self).__init__(driver)
        self.url = 'http://localhost/wordpress/'
        self.goTo()


    def getfirstPostLink(self):
        return self.driver.find_element(*self.firstPostLinkLocator)

