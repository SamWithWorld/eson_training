#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
from lib.LibLogin import LibLogin

class TestLogin(unittest.TestCase):

    def setUp(self):
        print 'Start test'
        self.driver =webdriver.Firefox()
        self.username = 'admin'
        self.passwd   = 'admin'
        self.data = [['oo','xx',u'错误：无效用户名。忘记密码？'],['admin','',u'错误：密码一栏为空。'],['','admin',u'错误：用户名一栏为空。']]


    def testLoginFailed(self):
        for username,passwd,tip in self.data:
            loginLib = LibLogin(self.driver)
            loginLib.login(username,passwd)
            self.assertIn('wp-login',self.driver.current_url)
            tip_div = self.driver.find_element_by_id('login_error')
            self.assertEqual(tip_div.text,tip)

#暂时注释掉了登陆用例
    def atestLogin(self):
        print 'testLogin'

        #实例化公用的登陆类
        libLogin = LibLogin(self.driver)
        #登陆操作
        libLogin.login(self.username,self.passwd)

        self.assertIn('wp-admin',self.driver.current_url)
        # 检查用户信息: 欢迎你，admin
        self.assertTrue(self.username in self.driver.find_element_by_css_selector('li#wp-admin-bar-my-account a').text)

    def tearDown(self):
        print 'End test'
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()
