#In[]
import pytest,allure
from config import Evn

def retrun_url(url):# 先產出全域變數url 用意, 是因pytest 在class 使用init 會失敗
    global sb_url
    sb_url = url
#In[]
class TestPytestOne:
    @allure.story('用戶故事描述：用例一')
    @allure.title('測試標題：用例一')
    @allure.description('測試用例描述：用例一')
    @allure.testcase('測試用例地址://www.baidu.com/')
    @allure.tag('測試用例標籤：用例一')
    def test_one(self,browser):
        url = sb_url
        if Evn().UrlConnect(url):
            browser.get(url)
            #allure.dynamic.title("登入網址是否健康測試 Pass!")
            assert True
        else:
            allure.dynamic.title("登入網址是否健康測試 Fail!")
            assert False
        browser.close()
    def Exec_Test(self):# 執行測試案例
        pytest.main(['-s', '-v', 'allure_test.py', '-q', '--alluredir', './reports'])
        Evn().Allure_Report()
        return 'ok'
'''
if __name__ == "__main__":
    pytest.main(['-s', '-v', 'allure_test.py', '-q', '--alluredir', './reports'])
    Evn().Allure_Report()
'''