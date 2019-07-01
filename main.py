import flask
from flask import request
import qrcode
from flask import render_template

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    # #第一步：获取要生成二维码的数据
    # data = flask.request.args.get('data')#"data"中的data是URL参数

    # #第二步：生成二维码图像
    # img = qrcode.make(data)
    # img.save("static/qr.jpg")
    
    # #第三步：在页面上显示二维码图片
    # return '<img src="/static/qr.jpg"/>' 

    return flask.render_template("qr_tool.html")

@app.route('/qr',methods=['POST'])
def qr():
    data = flask.request.form.get('data')
    #第二步：生成二维码图像
    img = qrcode.make(data)
    img.save("static/qr.jpg")
    
    #第三步：在页面上显示二维码图片
    return '<img src="/static/qr.jpg"/>' 



    
if __name__ == '__main__':
    #app.run(debug=True,host="0.0.0.0")
    app.run(debug=True)