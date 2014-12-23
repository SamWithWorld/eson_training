#coding:utf-8
from selenium import webdriver
import unittest

class CreatPost(unittest.TestCase):

    def setUp(self):
        self.driver =webdriver.Firefox()
        self.username = 'admin'
        self.passwd   = 'admin'

    def testLogin(self):

        #登陆操作
        self.login(self.username,self.passwd)

        self.assertIn('wp-admin',self.driver.current_url)
        # 检查用户信息 欢迎你，admin
        self.assertTrue(self.username in self.driver.find_element_by_css_selector('li#wp-admin-bar-my-account a').text)

    def tearDown(self):
        self.driver.quit()

    #登陆公用方法
    def login(self,username,passwd):
        dr = self.driver
        dr.get("http://localhost/wordpress/wp-login.php")
        usernameTxt = dr.find_element_by_id('user_login')
        usernameTxt.send_keys(username)
        passwdTxt = dr.find_element_by_id('user_pass')
        passwdTxt.send_keys(passwd)
        loginbtn = dr.find_element_by_id('wp-submit')
        loginbtn.click()


if __name__ == '__main__':
    unittest.main()
