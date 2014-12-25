#coding:utf-8
from selenium import webdriver
import unittest
import time
'''
增加了testCreatePost()方法
'''
class CreatPost(unittest.TestCase):

    def setUp(self):
        print 'Start test'
        self.driver =webdriver.Firefox()
        self.username = 'admin'
        self.passwd   = 'admin'

##    def testLogin(self):
##
##        #登陆操作
##        self.login(self.username,self.passwd)
##
##        self.assertIn('wp-admin',self.driver.current_url)
##        # 检查用户信息 欢迎你，admin
##        self.assertTrue(self.username in self.driver.find_element_by_css_selector('li#wp-admin-bar-my-account a').text)

    def testCreatePost(self):
        print 'CreatePost'
        self.login(self.username,self.passwd)

        #创建 新文章
        self.createPost() # title = self.createPost()

        #进入首页，进行断言
        self.driver.get('http://localhost/wordpress/')
        firstpost = self.driver.find_element_by_css_selector('h1.entry-title a')
        self.assertEqual(title,firstpost.text)

    def testDeletePost(self):
        '''
        1.先登陆，创建一篇文章，这样可以保证测试用例的健壮，删除时有数据可删
        '''
        #登陆
        self.login(self.username,self.passwd)
        self.createPost()

        #进入文章列表页面，准备删除文章
        self.driver.get("http://localhost/wordpress/wp-admin/edit.php")
        # xxxxxxxxxxxxxx

    def tearDown(self):
        print 'End test'
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

    def setContent(self,content):
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='"+content+"'"
        self.driver.execute_script(js)

    def createPost(self):
        # title 由当前时间组成，以免输入固定字符Sam、Test Content
        title = 'Sam'+time.strftime("%Y-%m-%d %H:%M:%S")
        content = 'Test Content'+time.strftime("%Y-%m-%d %H:%M:%S")

        #调用添加文章的方法
        self.createArticle(title,content)
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




if __name__ == '__main__':
    unittest.main()
