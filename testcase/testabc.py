#encoding:utf-8
__author__ = 'yongzhang'

import unittest,time
import HTMLTestRunner

class abc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('run before class')

    @classmethod
    def tearDownClass(cls):
        print('run after class ')

    def testA(self):
        self.assertEquals(2,2)
    # @unittest.skip('ddd')
    def testB(self):
        self.assertEquals(1,2)


def suit():
    suit_test = unittest.TestSuite()
    suit_test.addTest(abc('testA'))
    suit_test.addTest(abc('testB'))
    return suit_test

if __name__ == '__main__':
    fp = open('result.html','wb')
    html = HTMLTestRunner.HTMLTestRunner(fp,title='购物车项目测试报告',description='测试结果')
    testsuit = unittest.TestLoader().loadTestsFromTestCase(abc)
    # unittest.TextTestRunner().run(testsuit)
    html.run(testsuit)
    fp.close()

