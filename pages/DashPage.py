#coding:utf-8

from BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class DashPage(BasePage):

    greetingLocator = (By.CSS_SELECTOR,'li#wp-admin-bar-my-account .ab-item')

    def __init__(self,driver):
        super(DashPage,self).__init__(driver)


    def getGreetinglink(self):
        return self.driver.find_element(*self.greetingLocator)



if __name__ == '__main__':
    main()
