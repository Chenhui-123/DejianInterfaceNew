import unittest
import requests
import json
import sys
import os
import time
import HTMLTestRunner
base_path=os.getcwd()
sys.path.append(base_path)
#from unittest import mock
from Base.base_request import request_base
class TestMy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.host='https://dj.palmestore.com'
        print('--------------------this is setUpClass----------------------------')
    
    @classmethod
    def tearDownClass(cls):
        print('--------------------this is tearDownClass--------------------------')
    
    def setUp(self):
        print('--------------------this is setup--------------------------')

    def tearDown(self):
        print('--------------------this is teardown--------------------------')

    def test_login(self):
        url_login=self.host+'/dj_user/out/login/loginByPhoneV2?usr=j27871222&rgt=7&p1=V3WygQ4dlCADADL64yvBGhkY&pc=10&p2=124011&p3=17126056&p4=501656&p5=12&p6=&p7=__3e932cc0f202a00f&p9=2&p12=&p16=vivo+Y51A&p21=3&p22=5.1.1&p25=17126056&p26=22 HTTP/1.1'
        data={
            'channelId':'124011',
            'device':'vivo+Y51A',
            'imei':'__624900019789808',
            'pCode':'1',
            'phone':'11111111111',
            'sign':'w9HtPZD+vP+KcL5FYddDXkMrFiaHBJJEUFJ+1ZSa8VBjsPG93g2RRkSugoGUDFhIO0FhPtC+Ra/D13n0JYC/tmYhXToqHKvh/cCSSt6Z0FAfd7yHwl2s3VxUPoAhWNHjqIOTjrK4CmjJeKpR/wTsj2GIiVnXpdY3E6yPsgoYHAo=',
            'timestamp':'1595756193375',
            'userName':'j27871222',
            'versionId':'17126056'
        }
        res=request_base.send_method('post',url_login,data)
        print(res)
        res1=json.loads(res)
        self.assertEqual(res1['code'],0,msg='相等')
        print('测试通过')
        
    def test_myTab(self):
        url_myTab=self.host+'/zyuc/api/user/my/tab?sign=V3z41RGggYY2NhLOa1UZk4lUEEsvUP2LShuluZgZc/1I4lcw6h8mTh/NfCRqZTDoAt7wj+EgA7KuzyZJIGsa//YQDOPpfCV2FGB/JfqPLUdDK7VLng+W8gtw7BjYF2Xl4qLQOEMnEcim3KFY3Tb1vu23plv0YTruIO1bERLUB3w=&timestamp=1595756193640&usr=j28331372&zyeid=f622652b-52d3-4059-84e2-75b52d6dffad&usr=j28331372&rgt=7&p1=V3WygQ4dlCADADL64yvBGhkY&ku=j28331372&kt=7c589265807dc50ff4dc70ef29c4cbc1&pc=10&p2=124011&p3=17126056&p4=501656&p5=12&p6=&p7=__3e932cc0f202a00f&p9=2&p12=&p16=vivo+Y51A&p21=3&p22=5.1.1&p25=17126056&p26=22 HTTP/1.1'
        res=request_base.send_method('get',url_myTab,'')
        print(res)
        res1=json.loads(res)
        self.assertEqual(res1['code'],0,msg='错误')

    def test_yizhiGame(self):
        url_yizhiGame='https://api.gamecenter.viaweb.cn/list?vmedia=84'
        res=request_base.send_method('get',url_yizhiGame,'')
        #print(res)
        res1=json.loads(res)
        print(res1)
        print (len(res1['list']['others']))
        for i in res1['list']['others']:
            
            # print (res1['list']['others'][i]['c_end'])
            # s_icon=res1['list']['others'][i]['s_icon']
            # long_icon=res1['list']['others'][i]['long_icon']
            # clk_url=res1['list']['others'][i]['clk_url']
            # print (c_end)
            # print (s_icon)
            c_end=i.get('c_end')
            s_icon=i.get('s_icon')
            long_icon=i.get('long_icon')
            clk_url=i.get('clk_url')
            print (i.get('c_end'))
            c_start=i.get('c_start')
            
            #print(c_end.startswith('#'))
            #self.assertEqual(res1['code'],0,msg='错误')
            self.assertTrue(c_end.startswith('#'),msg='c_end的返回值需要以#开头')
            self.assertTrue(s_icon.startswith('http'),msg='s_icon的返回值需要以http开头')
            self.assertTrue(s_icon.endswith('.png') or s_icon.endswith('.jpg'),msg='s_icon的返回值需要以.png或者jpg结尾')
            self.assertTrue(long_icon.startswith('http'),msg='long_icon的返回值需要以http开头')
            self.assertTrue(long_icon.endswith('.png') or s_icon.endswith('.jpg'),msg='s_icon的返回值需要以.png或者jpg结尾')
            self.assertTrue(clk_url.startswith('http'),msg='clk_url的返回值需要以http开头')
            self.assertTrue(c_start.startswith('#'),msg='c_start的返回值需要以#开头')
            print ('开始又一次的遍历啦啦啦啦啦啦========================================================================')

        


