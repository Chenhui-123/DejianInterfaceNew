import unittest
import requests
import json
import sys
import os
import time
import HTMLTestRunner
base_path=os.getcwd()
sys.path.append(base_path)
from unittest import mock
from Base.base_request import request_base
class TestBookStore(unittest.TestCase):
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

      

    def test_frequencyDetailFemale(self):
        url_frequencyDetailFemale=self.host+'/zybook3/u/p/api.php?Act=frequencyDetail&key=MF0037&zyeid=0ad7a0cf-8ba4-4423-9adb-70006f663317&usr=j29095364&rgt=7&p1=XTpV6PJ%2FeDcDAOW8d1xT0h8e&pc=10&p2=124001&p3=17129056&p4=501656&p5=16&p6=&p7=__aea4c9dd6d4f9ccd&p9=2&p12=&p16=R9&p21=3&p22=6.0&p25=17129056&p26=23&p28='
        res=request_base.send_method('get',url_frequencyDetailFemale,'')
        res1=json.loads(res)
        self.assertEqual(res1['code'],0,msg='相等')
        print('测试通过')
    
    def test_frequencyFemale(self):
        url_frequencyFemale=self.host+'/zybk/api/channel/index?key=MF0037&page=1&repairReport=1&sign=cUzzulX4fITOcTxkGtvYRC9cyH3PSwPkhGKfJ+Jk91jp7+GF0gqC8T7Q93V8ce6pB5tk4p54fQXTnfys3aqPZuZAiRat7fLwwwHSaRCpxo03pvZ9zlPdBV02UieBzXPtpV0FtmCmnDgWYDF89HF06Jb+LtShR+2snxFChzFv0+Y=&timestamp=1597559946204&pluginVersion=107&a0=null&pk=null&today=0&zyeid=0ad7a0cf-8ba4-4423-9adb-70006f663317&usr=j29095364&rgt=7&p1=XTpV6PJ%2FeDcDAOW8d1xT0h8e&pc=10&p2=124001&p3=17129056&p4=501656&p5=16&p6=&p7=__aea4c9dd6d4f9ccd&p9=2&p12=&p16=R9&p21=3&p22=6.0&p25=17129056&p26=23&p28='
        res=request_base.send_method('get',url_frequencyFemale,'')
        res1=json.loads(res)
        self.assertEqual(res1['code'],0,msg='相等')
        # self.assertEqual(res['code'],0,msg='相等')
        print('测试通过')

    def test_frequencyDetailRecommended(self):
        url_frequencyDetailRecommended=self.host+'/zybook3/u/p/api.php?Act=frequencyDetail&key=MF0035&zyeid=0ad7a0cf-8ba4-4423-9adb-70006f663317&usr=j29095364&rgt=7&p1=XTpV6PJ%2FeDcDAOW8d1xT0h8e&pc=10&p2=124001&p3=17129056&p4=501656&p5=16&p6=&p7=__aea4c9dd6d4f9ccd&p9=2&p12=&p16=R9&p21=3&p22=6.0&p25=17129056&p26=23&p28='
        res=request_base.send_method('get',url_frequencyDetailRecommended,'')
        res1=json.loads(res)
        self.assertEqual(res1['code'],0,msg='相等')
        print('测试通过')

    def test_frequencyRecommended(self):
        url_frequencyRecommended=self.host+'/zybk/api/channel/index?key=MF0035&page=1&repairReport=1&sign=joSx8Xaa9qiAMbejBpJerNkOWx9eUV/sHr9fqp6opmCeYFyFZsTP9bi3AEkGo6o13qRWU35rCSEC4fY6B14am/rUStTjEwCBSWDo+AfzZAHM+lDyP07DFCtQtua1LkJYS0NOaBSe/SLI9ma6aPvwfUWizdmSZWWm7CyKEVtzRK0=&timestamp=1597564049136&pluginVersion=107&a0=null&pk=null&today=0&zyeid=0ad7a0cf-8ba4-4423-9adb-70006f663317&usr=j29095364&rgt=7&p1=XTpV6PJ%2FeDcDAOW8d1xT0h8e&pc=10&p2=124001&p3=17129056&p4=501656&p5=16&p6=&p7=__aea4c9dd6d4f9ccd&p9=2&p12=&p16=R9&p21=3&p22=6.0&p25=17129056&p26=23&p28='
        res=request_base.send_method('get',url_frequencyRecommended,'')
        res1=json.loads(res)
        self.assertEqual(res1['code'],0,msg='相等')
        print('测试通过')







        
