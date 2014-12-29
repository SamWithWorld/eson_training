#coding:utf-8

class LibLogin(object):

    def __init__(self,driver):
        self.driver = driver

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
    main()
