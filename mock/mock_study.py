from unittest import mock
import requests
import json

#url_BookUpdate = 'https://dj.palmestore.com/zyapi/bookstore/book/ireaderAndTingBookUpdate?zyeid=29e6309b-48d0-4f0d-9abf-b731d39fb0f6&usr=j23281661&rgt=7&p1=V3WygQ4dlCADADL64yvBGhkY&ku=j23281661&pc=10&p2=124002&p3=17120056&p4=501656&p5=12&p6=&p7=__3e932cc0f202a00f&p9=2&p12=&p16=vivo+Y51A&p21=3&p22=5.1.1&p25=17120056&p26=22'
url_push='https://dj.palmestore.com/dj_push/out/upload/report'

# param_BookUpdate = {
#     'bookIds' : '11286698,11302933,12148825,11845413,11772105,11303493,12092090,12151670,11286811,11793721,12178485'
# }

param_push = {
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

def post_request(url,data):
    res=requests.post(url,data).json()
    print (json.dumps(res,indent=4))
    return json.dumps(res,indent=4)
#post_request(url_BookUpdate,param_BookUpdate)
post_request(url_push,param_push)
