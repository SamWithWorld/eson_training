#coding:utf-8
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.BasePage import BasePage
import time

class PostFormPage(BasePage):

    titleLocator = (By.NAME,'post_title')
    publishBtnLocator = (By.NAME,'publish')
    samplePermaLinkLocator = (By.ID,"sample-permalink")

    def __init__(self,driver):
        super(PostFormPage,self).__init__(driver)
        self.url='http://localhost/wordpress/wp-admin/post-new.php'

    def getTitleTextField(self):
        return self.driver.find_element(*self.titleLocator)
    def getPublishBtn(self):
        return self.driver.find_element(*self.publishBtnLocator)
    def getSamplePermaLink(self):
        return self.driver.find_element(*self.samplePermaLinkLocator)

    def createPost(self,title='Default Title'):
        # content 由当前时间组成，以免输入固定字符Test Content
        #title = 'Sam'+time.strftime("%Y-%m-%d %H:%M:%S")
        content = 'Test Content'+time.strftime("%Y-%m-%d %H:%M:%S")

        #调用添加文章的方法
        return self.createArticle(title,content)
        #return title

    def createArticle(self,title,content):
        '''创建一篇文章'''

        # 进入写文章页面
        self.goTo()

        titleTxt = self.getTitleTextField()
        titleTxt.send_keys(title)

        #设置富文本框
        self.setContent(content)
        publishBtn = self.getPublishBtn()
        publishBtn.click()
        return self.fetchPostId()

    def setContent(self,content):
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='"+content+"'"
        self.driver.execute_script(js)

    def fetchPostId(self):
        postUrl = self.getSamplePermaLink().text

        #获得 文章的链接地址，如 http://localhost/wordpress/?p=25，并获得文章id号
        return postUrl.split("=")[-1]



