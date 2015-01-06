#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
##from lib.LibLogin import LibLogin
from pages.LoginPage import LoginPage
from pages.DashPage import DashPage

class TestLogin(unittest.TestCase):

    def setUp(self):
        print 'Start test'
        self.driver =webdriver.Firefox()
        self.username = 'admin'
        self.passwd   = 'admin'
        self.loginPageUrl = 'http://localhost/wordpress/wp-login.php'

#暂时注释掉了登陆用例
    def testLogin(self):
        print 'testLogin'
        loginPage = LoginPage(self.driver,self.loginPageUrl)

        # 方法返回页面，即现实中的页面跳转操作
        dashboardPage =loginPage.login(self.username,self.passwd)

        self.assertIn('wp-admin',dashboardPage.currentUrl())
        # 检查用户信息: 欢迎你，admin
##        self.assertTrue(self.username in self.driver.find_element_by_css_selector('li#wp-admin-bar-my-account a').text)
        self.assertIn(self.username,dashboardPage.getGreetinglink().text)

    def tearDown(self):
        print 'End test'
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
