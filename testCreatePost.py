#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
from lib.LibLogin import LibLogin


class TestCreatPost(unittest.TestCase):

    def setUp(self):
        print 'Start test'
        self.driver =webdriver.Firefox()
        self.username = 'admin'
        self.passwd   = 'admin'

    def testCreatePost(self):
        print 'testCreatePost'

        lib_login = LibLogin(self.driver)
        lib_login.login(self.username,self.passwd)

        # title 由当前时间组成，以免输入固定字符Sam、Test Content
        title = 'Sam'+time.strftime("%Y-%m-%d %H:%M:%S")

        #创建 新文章
        #self.createPost()
        self.createPost(title)

        #进入首页，进行断言
        self.driver.get('http://localhost/wordpress/')
        firstpost = self.driver.find_element_by_css_selector('h1.entry-title a')
        self.assertEqual(title,firstpost.text)


    def tearDown(self):
        print 'End test'
        self.driver.quit()

    def setContent(self,content):
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='"+content+"'"
        self.driver.execute_script(js)

    def createPost(self,title='Default Title'):
        # content 由当前时间组成，以免输入固定字符Test Content
        #title = 'Sam'+time.strftime("%Y-%m-%d %H:%M:%S")
        content = 'Test Content'+time.strftime("%Y-%m-%d %H:%M:%S")

        #调用添加文章的方法
        return self.createArticle(title,content)
        #return title

    def createArticle(self,title,content):
        #创建一篇文章
        # 进入写文章页面
        self.driver.get('http://localhost/wordpress/wp-admin/post-new.php')

        titleTxt = self.driver.find_element_by_id('title')
        titleTxt.send_keys(title)

        #设置富文本框
        self.setContent(content)
        publishBtn = self.driver.find_element_by_id('publish')
        publishBtn.click()

        return self.fetchPostId()

if __name__ == '__main__':
    unittest.main()
