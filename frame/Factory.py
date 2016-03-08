#encoding:utf-8
__author__ = 'yongzhang'
from UIFrameworks.frame import AppPage,WebPage

class Factory :
    @classmethod
    def createAutomation(cls,page):
        page = page.lower()
        if page == 'web':
            return WebPage()
        if page == 'app':
            return AppPage()
