#encoding:utf-8
__author__ = 'yongzhang'
from UIFrameworks.frame import AutomationPage


class WebPage(AutomationPage):
    def __str__(self):
        return 'web'

    def __init__(self,driver):
        self.driver=driver

    def goTo(self,base_url):
        self.driver.get(base_url)

    def getCurrentUrl(self):
        return self.driver.current_url
