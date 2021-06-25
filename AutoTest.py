from selenium import webdriver
import unittest
import HTMLTestRunner
from config import Evn
import os

class WebApiTest(unittest.TestCase):#之後APi測試可用
    def __init__(self,url):
        self.url = url 

class WebAutoTest(unittest.TestCase):
    '''Pc頁面自動化測試'''
    def __init__(self,case,url):
        self.case = super().__init__(case)# 不複寫的話,會爆 AttributeError: 'WebAutoTest2' object has no attribute '_testMethodName'
        self.url = url 
    @classmethod
    def setUpClass(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])# 防止打印一些无用的日志
        self.dr = webdriver.Chrome(options=self.option)
    def test_url(self):
        '''URL測試'''
        if Evn().UrlConnect(self.url):
            self.dr.get(self.url)
            #allure.dynamic.title("登入網址是否健康測試 Pass!")
            print('ok')
            assert True
        else:
            assert False
    @classmethod
    def tearDownClass(self):
        self.dr.quit()
def suite_test(url):
    suite = unittest.TestSuite()
    TestCase_WebAuto = [WebAutoTest(case='test_url',url=url)]
    suite.addTests(TestCase_WebAuto)
    project_path = os.getcwd()  # 專案路徑
    reportHtml_Path = project_path + r"\templates\report.html"  # report.html 絕對路徑
    filename = reportHtml_Path
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'測試報告',
        description=f'URL: %s'%url,
    )
    runner.run(suite)
    fp.close()