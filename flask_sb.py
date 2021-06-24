

from flask import Flask, render_template, request,redirect,url_for,abort
import requests
from config import Evn
import allure_test
app = Flask(__name__)  # name 為模塊名稱

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/AutoTest', methods=['GET','POST'])
def AutoTest():
    url_dict = Evn().url_dict
    if request.method == "POST":
        url_index =  request.form['url'] # 頁面 獲得url value, 是 str
        sb_url = url_dict[int(url_index)]# 須轉str 
        allure_test.retrun_url(sb_url)
        return allure_test.TestPytestOne().Exec_Test()
    return render_template('AutoTest.html',url_dict=url_dict)
@app.route('/Allure_Report',methods=["GET"])
def Allure_Report():
    return render_template('allure_report.html')
@app.route('/error')  # 錯誤處理
def error():
    abort(404)
@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('404.html'), 404

'''
get_json 和 get_data 這兩個路由, 是產生自動化測試報告, 
app.js 要取得 widgets 和 data路徑下的 json檔
不能從html src加入, 因為 allure產出的 app.js ,已經寫死取得的路境

'''
@app.route('/widgets/<filename>.json')
def get_json(filename):
  return app.send_static_file('./allure_report/widgets/%s.json'%filename)
@app.route('/data/<filename>.json')
def get_data(filename):
  return app.send_static_file('./allure_report/data/%s.json'%filename)
if __name__ == "__main__":

    app.config['TESTING'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(host="0.0.0.0", debug=True, port=4444, threaded=True)