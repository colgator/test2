

from flask import Flask, render_template, request,redirect,url_for,abort
import requests
from config import Evn
#import AutoTest unittest架構
import allure_test
app = Flask(__name__)  # name 為模塊名稱 

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/SbAutoTest', methods=['GET','POST'])
def SbAutoTest():
    url_dict = Evn().url_dict
    if request.method == "POST":
        url_index =  request.form['url'] # 頁面 獲得url value, 是 str
        sb_url = url_dict[int(url_index)]# 須轉str 
        allure_test.retrun_url(sb_url)
        return allure_test.TestPytestOne().Exec_Test()
        '''
        # AutoTest.suite_test(url=sb_url) unittest架構
        #return redirect('report')
        '''
        
    return render_template('AutoTest.html',url_dict=url_dict)

@app.route('/report',methods=["GET"])
def report():
    return render_template('report.html')
@app.route('/error')  # 錯誤處理
def error():
    abort(404)
@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('404.html'), 404


if __name__ == "__main__":

    app.config['TESTING'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(host="0.0.0.0", debug=True, port=4444, threaded=True)