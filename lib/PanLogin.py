#encoding:utf-8
__author__ = 'yongzhang'

from selenium.webdriver.common.by import By
from UIFrameworks.frame.AppPage import AppPage

import time
class PanLogin(AppPage):

    login_loc=(By.ID,'com.meilishuo:id/acz')
    userName_loc=(By.ID,'com.meilishuo:id/aby')
    password_loc=(By.ID,'com.meilishuo:id/abz')
    loginButton_loc=(By.ID,'com.meilishuo:id/ac0')


    def clickLogin(self):
        self.findElement(*self.login_loc).click()
        time.sleep(2)

    def inputUserName(self,username):
        inputstring = self.findElement(*self.userName_loc)
        inputstring.clear()
        inputstring.send_keys(username)
        time.sleep(2)

    def inputPasswd(self,password):
        inputstring = self.findElement(*self.password_loc)
        inputstring.clear()
        inputstring.send_keys(password)
        time.sleep(2)

    def clickLoginButton(self):
        self.findElement(*self.loginButton_loc).click()
        time.sleep(2)

    def login(self,username='admin',password='admin'):
        self.clickLogin()
        self.inputUserName(username)
        self.inputPasswd(password)
        self.clickLoginButton()


