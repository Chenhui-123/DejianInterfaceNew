import requests
#import json
url = 'https://dj.palmestore.com/zyapi/bookstore/book/ireaderAndTingBookUpdate?zyeid=29e6309b-48d0-4f0d-9abf-b731d39fb0f6&usr=j23281661&rgt=7&p1=V3WygQ4dlCADADL64yvBGhkY&ku=j23281661&pc=10&p2=124002&p3=17120056&p4=501656&p5=12&p6=&p7=__3e932cc0f202a00f&p9=2&p12=&p16=vivo+Y51A&p21=3&p22=5.1.1&p25=17120056&p26=22'
payload = {
    "zyeid":"29e6309b-48d0-4f0d-9abf-b731d39fb0f6",
    "usr":"j23281661",
    "rgt":"7",
    "p1":"V3WygQ4dlCADADL64yvBGhkY",
    "ku":"j23281661",
    "pc":"10",
    "p2":"124002",
    "p3":"17120056",
    "p4":"501656",
    "p5":"12",
    #"p6":"",
    "p7":"__3e932cc0f202a00f",
    "p9":"2",
    #"p12":"",	
    "p16":"vivo Y51A",
    "p21":3,
    "p22":"5.1.1",
    "p25":"17120056",
    "p26":22
}
headers = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Content-Length' : '106',
    'Host' : 'dj.palmestore.com',
    'Connection' : 'Keep-Alive',
    'Accept-Encoding' : 'gzip',
    'User-Agent' : 'okhttp/3.11.0'

}



param = {
    'bookIds' : '11286698,11302933,12148825,11845413,11772105,11303493,12092090,12151670,11286811,11793721,12178485'
}

res=requests.post(url,data=param)
print(res.text)
print('======================================================')
json_res= res.json()
print (json_res['code'])
#print (json.dumps(json_res,indent=4))

url1='https://dj.palmestore.com/zybk/api/ad/adconfig?ip=61.48.177.22&timestamp=1589636053372&pluginVersion=69&zyeid=29e6309b-48d0-4f0d-9abf-b731d39fb0f6&usr=j23281661&rgt=7&p1=V3WygQ4dlCADADL64yvBGhkY&ku=j23281661&pc=10&p2=124002&p3=17120056&p4=501656&p5=12&p6=&p7=__3e932cc0f202a00f&p9=2&p12=&p16=vivo+Y51A&p21=3&p22=5.1.1&p25=17120056&p26=22'
res1= requests.get(url1)
#print (res1)
# json_res1=res1.json()
# print (json.dumps(json_res1,indent=4))
