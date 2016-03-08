#encoding:utf-8
__author__ = 'yongzhang'
from selenium.webdriver.support.expected_conditions import NoSuchElementException

class AutomationPage:

    def __str__(self):
        return 'page'

    def findElement(self,*loc):
        try:
            return self.driver.find_element(*loc)
        except(NoSuchElementException,KeyError,ValueError) as e:
            print('Error details :%s'%(e.args[0]))

    def sendKeys(self,*loc,input_string):
        pass