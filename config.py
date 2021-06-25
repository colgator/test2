import requests,subprocess
class Evn:
    def __init__(self):
        self.url_dict = {0: 'http://www.athena000.com/NewIndex',
        1:'http://qasb.athena000.com:42106/NewIndex',
        2:'http://qasb.athena000.com:43100/NewIndex',
        3:'http://qasb.athena000.com:42104/NewIndex'}
        self.r = requests.Session()
        self.headers = { 'User-Agent':  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.100 Safari/537.36"}

    def UrlConnect(self,url,assert_text='athena000'):#確認url 連現狀態,url_key參數為 self.url key
        response = self.r.get(url,headers=self.headers)
        if assert_text in response.text:
            return True
        return False
    def Allure_Report(self):# 跑完生成allure json檔後, 執行該方式 去生成報告
        popen_path = 'allure generate reports -o static/allure_report --clean'
        p = subprocess.Popen(popen_path,stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
        shell=True, universal_newlines=True)
        return p.communicate()