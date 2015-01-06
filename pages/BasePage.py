#coding:utf-8
from selenium import webdriver

class BasePage(object):
    '''
	BasePage封装所有页面的通用的方法,例如driver, url
    '''
    def __init__(self,driver):
        self.driver = driver
##        self.url = url

    def goTo(self):
        self.driver.get(self.url)

    def currentUrl(self):
        return self.driver.current_url

if __name__ == '__main__':
    main()
