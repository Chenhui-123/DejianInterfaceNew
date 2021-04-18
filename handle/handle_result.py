import configparser
import os
import sys
import json
import deepdiff
base_path=os.getcwd()
sys.path.append(base_path)
from handle.handle_json import handJson
class HandleResult:
    def __init__(self):
        pass
    '''
    [{'0': 'ok'}, {'1': 'no'}, {'2': 'iiiiiiiiiiiii'}]
    '''
    def get_value(self,url,code):
        data= handJson.get_value(url)
        print("get_value url:", url, ",code:", code,",code type:",type(code),",data:", data)
        if data!=None:
            for i in data: #每次循环都把data列表中的值赋给i,赋值从索引号0开始#循环的语句需要缩进
                message=i.get(str(code))
                if message:
                    return message
                if message=='':
                    return message
                
            print('未获取到message值')
            return None
        else:
            print('未获取到data值')
            return None
    
    def handle_result_json(self,dict1,dict2):
        # dict1={"aaa":"AAA","bbb":"BBBB","CC":[{"11":"22"},{"33":"44"}]}
        # dict2={"aaa":"AAAA","bbb":"BBBB1","CC":[{"11":"222"},{"33":"44"}]}
        # dict3={"bbb":"BBBB","CC":[{"11":"22"},{"33":"44"}],"EE":"eee"}
        #print(deepdiff.DeepDiff(dict3,dict2,ignore_order=True).to_dict())
        cmp_dict=deepdiff.DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        print(cmp_dict)
        if cmp_dict.get("dictionary_item_added") or cmp_dict.get("dictionary_item_removed"):
            print("case执行失败")
            return False
        else:
            print("case执行成功")
            return True
        pass

    def get_result_json(self,url):
        data= handJson.get_value(url,"/config/result.json")
        print("get_result_json:", url, "url type:",type(url))
        if data!=None:
            
            return data
        else:
            return None

handleResult=HandleResult()
if __name__=='__main__':
    dict1={"aaa":"AAAA","bbb":"BBBB","CC":[{"11":"222"},{"33":"44"}]}
    dict2={"bbb":"BBBB","CC":[{"11":"222"},{"33":"44"}]}
    handleResult=HandleResult()
    print(handleResult.handle_result_json(dict1,dict2))
    
    #print(handleResult.get_value('/zyuc/api/user/my/tab?sign=V3z41RGggYY2NhLOa1UZk4lUEEsvUP2LShuluZgZc/1I4lcw6h8mTh/NfCRqZTDoAt7wj+EgA7KuzyZJIGsa//YQDOPpfCV2FGB/JfqPLUdDK7VLng+W8gtw7BjYF2Xl4qLQOEMnEcim3KFY3Tb1vu23plv0YTruIO1bERLUB3w=&timestamp=1595756193640&usr=j28331372&zyeid=f622652b-52d3-4059-84e2-75b52d6dffad&usr=j28331372&rgt=7&p1=V3WygQ4dlCADADL64yvBGhkY&ku=j28331372&kt=7c589265807dc50ff4dc70ef29c4cbc1&pc=10&p2=124011&p3=17126056&p4=501656&p5=12&p6=&p7=__3e932cc0f202a00f&p9=2&p12=&p16=vivo+Y51A&p21=3&p22=5.1.1&p25=17126056&p26=22 HTTP/1.1',3))





