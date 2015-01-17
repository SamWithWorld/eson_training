#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest
import time,string
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
        self.userData = [['oo','xx',u'错误：无效用户名。忘记密码？'],['admin','',u'错误：密码一栏为空。'],['','admin',u'错误：用户名一栏为空。']]

    def testLoginFailed(self):
        print 'testLoginFailed'
        for name,passwd,tip in self.userData:
            print string.ljust(name,8),string.ljust(passwd,8),tip,'0'*20

            loginPage = LoginPage(self.driver,self.loginPageUrl)

            # 方法返回页面，即现实中的页面跳转操作
            lPage =loginPage.loginFailed(name,passwd)

            # 登陆失败仍停留在登陆页面
            self.assertIn('wp-login',lPage.currentUrl())

            # 登录失败，调用loginErrorDiv方法，检查登陆失败错误信息
            self.assertEqual(lPage.loginErrorDiv().text,tip)

    def testLogin(self):
        print 'testLogin'
        loginPage = LoginPage(self.driver,self.loginPageUrl)

        # 方法返回页面，即现实中的页面跳转操作
        dashboardPage =loginPage.login(self.username,self.passwd)

        self.assertIn('wp-admin',dashboardPage.currentUrl())
        # 检查用户信息: 欢迎你，admin
        self.assertIn(self.username,dashboardPage.getGreetinglink().text)


    def tearDown(self):
        print 'End test'
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
