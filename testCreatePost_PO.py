#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
from pages.LoginPage import LoginPage
from pages.PostFormPage import PostFormPage
from pages.HomePage import HomePage

class TestCreatPost(unittest.TestCase):

    def setUp(self):
        print 'Start test'
        self.driver =webdriver.Firefox()
        self.username = 'admin'
        self.passwd   = 'admin'
##        self.homePageUrl = 'http://localhost/wordpress/'
        self.loginPageUrl = 'http://localhost/wordpress/wp-login.php'

    def testCreatePost(self):
        print 'testCreatePost'

        #登陆
        theLoginPage = LoginPage(self.driver,self.loginPageUrl)
        theLoginPage.login(self.username,self.passwd)

        # title 由当前时间组成，以免输入固定字符Sam、Test Content
        title = 'Sam'+time.strftime("%Y-%m-%d %H:%M:%S")

        #创建 新文章
        createPostPage = PostFormPage(self.driver)
        createPostPage.createPost(title)

        #进入首页，进行断言
        theHomePage = HomePage(self.driver)
        self.assertEqual(title,theHomePage.getfirstPostLink().text)

    def tearDown(self):
        print 'End test'
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
