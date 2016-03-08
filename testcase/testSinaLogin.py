#encoding:utf-8
__author__ = 'yongzhang'
from UIFrameworks.lib import PanLogin
from UIFrameworks.frame import AppPage
import unittest,HTMLTestRunner

class testSinaLogin(unittest.TestCase,PanLogin.PanLogin,AppPage.AppPage):

    def setUp(self):
        self.getDesiredcaps('81df6d6','4.4','com.meilishuo','.app.activity.MainActivity')

    def tearDown(self):
        self.driver.quit()

    def testSinaLogin(self):
        # self.login('18910351512','Mlsmima')
        print(self.ScreenSize)

if __name__ == '__main__':
    report = open('../report.html','wb')
    testrunner = HTMLTestRunner.HTMLTestRunner(report,verbosity=2,title='new frame',description='dddddd')
    testsuit = unittest.makeSuite(testSinaLogin)
    testrunner.run(testsuit)