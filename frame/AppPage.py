#encoding:utf-8
__author__ = 'yongzhang'
from UIFrameworks.frame import AutomationPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
import os.path,time
from UIFrameworks.util import tools


class AppPage(AutomationPage.AutomationPage):

    top_locs = ['android.widget.LinearLayout','android.widget.FrameLayout']

    def __str__(self):
        return 'app'

    def __init__(self):
        pass

    def getDesiredcaps(self,deviceName,version,package,activity):
        """
        :param version: 设备版本
        :param deviceName: 设备名称
        :param package: apk包名称
        :param activity: apk的activity
        :return:android初始化信息
        """
        PATH=lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']=version
        # desired_caps['deviceName']='Android Emulator'
        desired_caps['deviceName']=deviceName
        desired_caps['appPackage']=package
        desired_caps['appActivity']=activity
        desired_caps['waitappActivity']='android.webkit.WebView'
        desired_caps['browserName']=''
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.getSize()
        self.driver.implicitly_wait(30)

    def getSize(self):
        ScreenSize = []
        for top_loc in self.top_locs:
            try:
                time.sleep(1)
                elements = self.driver.find_elements_by_class_name(top_loc)
            except NoSuchElementException as e :
                continue
            if elements:
                ScreenSize.append(elements[0].size)
        if(len(ScreenSize)):
            self.ScreenSize = tools.getMaxDict(ScreenSize)
        else:
            print(u'获取屏幕尺寸失败')

    def toLeft(self,*loc):
        self.findElement(*loc)
        self.driver.swipe()
