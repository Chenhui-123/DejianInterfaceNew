import unittest
import requests
import json
import HTMLTestRunner
from unittest import mock
class TestPush(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('this is setupclass===============')
        cls.param_push1={
            'appKey':'fe5fa891b376498c857e9e7dd080d2e2',
            'deviceToken':'CN_2eaf031de4c868bd8e83d6f2aecf1f52',
            'platform':'android',
            'pushChannel':'oppo',
            'sign':'r0jI8BET4Oy5mFxbN0KIMWA41dpgIB9UqnvvMXqeqmy/lclyHawPgoiSwXTf6uCK1BVYWrEzNiIJvZvPjaus6/9AugwFe45TsfLn8Mge/8MO9VrFLIosQ++YPXH5qaVPampBPyznzY15i07/wbsDcm+LXYmQsxdWNlmnuHdgNl0=',
            'timestamp':'1593861671148',
            'user':'j27566808',
            'pc':'10',
            'p2':'124011',
            'p3':'17124056',
            'p4':'501656',
            'p5':'16',
            'p6':'',	
            'p7':'__8b29c1f8c090c577',
            'p9':'2',
            'p12':'',	
            'p16':'OPPO A37m',
            'p21':'3',
            'p22':'5.1',
            'p25':'17124056',
            'p26':'22',
            'zyeid':'5d94300a-dcb1-48b5-be66-826b58623eac',
            'usr':'j27566808',
            'rgt':'7',
            'p1':'Wtbq+hAtvbEDAFr/gA/tJBmY',
            'ku':'j27566808',
            'kt':'520a979cc140a7bcf46af6a73787e7c7'
        }
    @classmethod
    def tearDownClass(cls):
        print('this is teardownclass=============')
        
    def setUp(self):
        print('case开始执行')
        
    def tearDown(self):
        print('case执行结束')
    def post_request(self,url,data):
        res=requests.post(url,data).json()
        # print (json.dumps(res,indent=4))
        return json.dumps(res,indent=4)
    @unittest.skipIf(4>5,'条件为真的时候不执行push接口测试用例')
    def test_01(self):
        url_push='https://dj.palmestore.com/dj_push/out/upload/report'
        param_push={
            'appKey':'fe5fa891b376498c857e9e7dd080d2e2',
            'deviceToken':'CN_2eaf031de4c868bd8e83d6f2aecf1f52',
            'platform':'android',
            'pushChannel':'oppo',
            'sign':'r0jI8BET4Oy5mFxbN0KIMWA41dpgIB9UqnvvMXqeqmy/lclyHawPgoiSwXTf6uCK1BVYWrEzNiIJvZvPjaus6/9AugwFe45TsfLn8Mge/8MO9VrFLIosQ++YPXH5qaVPampBPyznzY15i07/wbsDcm+LXYmQsxdWNlmnuHdgNl0=',
            'timestamp':'1593861671148',
            'user':'j27566808',
            'pc':'10',
            'p2':'124011',
            'p3':'17124056',
            'p4':'501656',
            'p5':'16',
            'p6':'',	
            'p7':'__8b29c1f8c090c577',
            'p9':'2',
            'p12':'',	
            'p16':'OPPO A37m',
            'p21':'3',
            'p22':'5.1',
            'p25':'17124056',
            'p26':'22',
            'zyeid':'5d94300a-dcb1-48b5-be66-826b58623eac',
            'usr':'j27566808',
            'rgt':'7',
            'p1':'Wtbq+hAtvbEDAFr/gA/tJBmY',
            'ku':'j27566808',
            'kt':'520a979cc140a7bcf46af6a73787e7c7'
        }
        res=self.post_request(url_push,param_push)
        sucess_test=mock.Mock(return_value=res)
        # post_request=sucess_test
        # res=post_request
        
        self.assertEqual(res,sucess_test())
        print('执行push接口测试用例')
    def test_02(self):
        data={
            'name':'chenhui',
            'age':12
        }
        self.assertDictEqual(self.param_push1,data,msg='两个字典不相等')

    
if __name__=='__main__':
    unittest.main()