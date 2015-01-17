#coding:utf-8
from selenium import webdriver
from BasePage import BasePage
from selenium.webdriver.common.by import By
from DashPage import DashPage
class LoginPage(BasePage):

    usernameLocator = (By.ID,'user_login')
    passwdLocator = (By.ID,'user_pass')
    loginButtonLocator = (By.ID,'wp-submit')
    loginErrorLocator = (By.ID,'login_error')

    def __init__(self,driver,url):
        super(LoginPage,self).__init__(driver)
        self.url    = url
        self.goTo()

    def getuserTextField(self):
        return self.driver.find_element(*self.usernameLocator)

    def getpasswdTextField(self):
        return self.driver.find_element(*self.passwdLocator)

    def getsubmitButton(self):
        return self.driver.find_element(*self.loginButtonLocator)

    def loginErrorDiv(self):
        return self.driver.find_element(*self.loginErrorLocator)

    def login(self,username,passwd):
        #登陆成功，返回一个DashPage实例
        self.doLoginStep(username,passwd)
        return DashPage(self.driver)

    #登陆失败的操作单独写一个方法
    def loginFailed(self,username,passwd):
        self.doLoginStep(username,passwd)
        return self

    def doLoginStep(self,username,passwd):
        self.getuserTextField().send_keys(username)
        self.getpasswdTextField().send_keys(passwd)
        self.getsubmitButton().click()


if __name__ == '__main__':
    main()
