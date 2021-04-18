#coding=utf-8
from flask import Flask
import json
from flask import request
app=Flask(__name__)
@app.route('/')
def Home():
    data=json.dumps({
        'username':'chenhui',
        'password':'123456'
    })
    return data
@app.route('/dj_user/out/login/loginByPhoneV2',methods=['GET'])
def Login():
    username=request.args.get("username")
    password=request.args.get("password")
    if username and password:
        data=json.dumps({
            "username":username,
            "password":password,
            "msg":"请求成功",
            "code":200
        })
    else:
        data=json.dumps({
            "msg":"请传参数"
        })
    return data



#https://dj.palmestore.com/dj_user/out/login/loginByPhoneV2?zyeid=04495502-fac7-4825-853e-68f64f6dcbb5&usr=j24839612&rgt=7&p1=V3WygQ4dlCADADL64yvBGhkY&pc=10&p2=124008&p3=17120056&p4=501656&p5=12&p6=&p7=__3e932cc0f202a00f&p9=2&p12=&p16=vivo+Y51A&p21=3&p22=5.1.1&p25=17120056&p26=22

@app.route('/dj_user/out/login/post_loginByPhoneV2',methods=['POST'])
def post_login():
    request_method=request.method
    if request_method=='POST':
        username=request.form.get("username")
        password=request.form.get("password")
        data=json.dumps({
            "username":username,
            "password":password,
            "msg":"请求成功",
            "code":200
        })

    else:
         data=json.dumps({
            "msg":"请求方式不合法"
        })
    return data



if __name__=='__main__':
    #print login()
    app.run()