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

#暂时注释掉了登陆用例
    def testLogin(self):
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
