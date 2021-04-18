#coding=utf-8
import requests
import json
class BaseRequest:
    def send_post(self,url,data):
        '''
        发送post请求
        '''
        res=requests.post(url=url,data=data)
        return res
    
    def send_get(self,url,data):
        '''
        发送get请求
        '''
        res=requests.get(url=url,params=data)
        return res

    def send_method(self,method,url,data):
        '''
        执行方法，传递method、url、data
    
        '''

        if method=='post':
            res=self.send_post(url,data).json()
        else:
            res=self.send_get(url,data).json()
        try:
            res=json.dumps(res,indent=4)
        except:
            print('编码成json字符串报错')
        return res

request_base=BaseRequest()