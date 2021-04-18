import os
import sys
base_path=os.getcwd()
sys.path.append(base_path)
import json

class HandJson:
    def __init__(self):
        pass
    def read_json(self,file_name=None):
        if file_name==None:
            file_path=base_path+"/config/code_message.json"
        else:
            file_path=base_path+file_name
        with open(file_path,'r',encoding='UTF-8') as f:
            data=json.load(f)
            return data
    def get_value(self,key,file_name=None):
        data=self.read_json(file_name)
        return data.get(key)
handJson=HandJson()
if __name__=='__main__':
    handJson=HandJson()
    print(base_path)
    #print(handJson.read_json("/config/url_data.json"))
    print(handJson.get_value('/dj_user/out/login/loginByPhoneV2?usr=j27871222&rgt=7&p1=V3WygQ4dlCADADL64yvBGhkY&pc=10&p2=124011&p3=17126056&p4=501656&p5=12&p6=&p7=__3e932cc0f202a00f&p9=2&p12=&p16=vivo+Y51A&p21=3&p22=5.1.1&p25=17126056&p26=22 HTTP/1.1'))
    # a=''
    # if a:
    #     print("=======================")
               


