#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
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


    def testCreatePost(self):
        print 'testCreatePost'
        self.login(self.username,self.passwd)

        # title 由当前时间组成，以免输入固定字符Sam、Test Content
        title = 'Sam'+time.strftime("%Y-%m-%d %H:%M:%S")

        #创建 新文章
        #self.createPost()
        self.createPost(title)

        #进入首页，进行断言
        self.driver.get('http://localhost/wordpress/')
        firstpost = self.driver.find_element_by_css_selector('h1.entry-title a')
        self.assertEqual(title,firstpost.text)

    def testDeletePost(self):
        print 'testDeletePost'
        '''
        1.先登陆，创建一篇文章，这样可以保证测试用例的健壮，删除时有数据可删
        '''
        #登陆
        self.login(self.username,self.passwd)
        #创建一篇文章，并获取文章id
        post_id = self.createPost()

        #进入 所有文章 页面，准备删除文章
        self.driver.get("http://localhost/wordpress/wp-admin/edit.php")
        #拼接文章id
        rowId = 'post-'+post_id
        # 定位新创建的文章，准备删除
        row = self.driver.find_element_by_id(rowId)
        ActionChains(self.driver).move_to_element(row).perform()
        #定位 移至回收站 元素
        trashlink = row.find_element_by_css_selector('span.trash a')
        trashlink.click()
        self.assertFalse(self.isPostRowExists(rowId))

    def isPostRowExists(self,rowId):
        try:
            self.driver.find_element_by_id(rowId)
            return True

        except NoSuchElementException as e:
            return False

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

    def fetchPostId(self):
        postUrl = self.driver.find_element_by_id("sample-permalink").text

        #获得 文章的链接地址，如 http://localhost/wordpress/?p=25，并获得文章id号
        return postUrl.split("=")[-1]

if __name__ == '__main__':
    unittest.main()
