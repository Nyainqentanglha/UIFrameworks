#encoding:utf-8
__author__ = 'yongzhang'

import unittest,os.path
from UIFrameworks import testcase,lib,frame
import HTMLTestRunner
import time

def getCase():

    suits = []
    testsuit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),'testcase'))
    for suit in discover:
        for case in suit:
            testsuit.addTests(case)
    return testsuit

def mksiut():
    pass

def run():
    report_name = 'report_'+time.strftime("%Y%m%d_%H:%M:%S", time.localtime())+'.html'
    fp = open(os.path.join(os.path.dirname(__file__),'report',report_name),'wb')
    htmlrunner = HTMLTestRunner.HTMLTestRunner(fp,description='all test',title='高步',verbosity=3)
    suits = getCase()
    htmlrunner.run(suits)
    fp.close()

if __name__ == '__main__':
    run()