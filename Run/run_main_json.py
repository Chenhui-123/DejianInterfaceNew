import sys
import os
import json
base_path=os.getcwd()
sys.path.append(base_path)

from handle.handle_ini import handleIni
from Base.base_request import request_base
from handle.handle_json import handJson
from handle.handle_result import handleResult
from handle.handle_excel import handle_excel
from util.post_email import postEmail
class RunMainJson:
    def __init__(self):
        self.host_server=handleIni.get_value('host')
        pass

    def run_case(self):
        '''
        获取url_data.json中的数据
        '''
        
        file_name="/config/url_data.json"
        url_data_dict=handJson.read_json(file_name)
        print("====================================================")
        print(url_data_dict)
        print("=====================================================")
        #handJson.get_value(key,file_path)
        i=0
        for key in url_data_dict:
            i=i+1
            '''
            每个接口的url为key
            值为列表 ['我的_登录', '是', 'post', '', '', 'code+message', '']
            '''
            url_data=url_data_dict.get(key)
            if key!='https://api.gamecenter.viaweb.cn/list?vmedia=85':

                url=self.host_server+key
                method=url_data[2]
                data=url_data[3]
                res_json=request_base.send_method(method,url,data)
                res_dict=json.loads(res_json)
                code=res_dict.get('code')
                print(type(code))
                msg=res_dict.get('msg')
            else:
                url=key
                method=url_data[2]
                data=url_data[3]
                res_json=request_base.send_method(method,url,data)
                res_dict=json.loads(res_json)
                

            '''
            通过预期结果方式、预期结果与实际的结果进行对比。比较用例是通过还是失败
            '''
            excepect_method=url_data[5]
            if excepect_method=='code+message':
                excepect_message=handleResult.get_value(key,code)
                if excepect_message==msg:
                    print("接口测试通过")
                    handle_excel.excel_write_data(i+1,10,"通过")
                else:
                    print("接口测试不通过")
                    handle_excel.excel_write_data(i+1,10,"失败")
                    handle_excel.excel_write_data(i+1,11,res_json)
            if excepect_method=='code':
                if url_data[6]==str(code):
                    print("接口测试通过")
                    handle_excel.excel_write_data(i+1,10,"通过")
                else:
                    print("接口测试不通过")
                    handle_excel.excel_write_data(i+1,10,"失败")
                    handle_excel.excel_write_data(i+1,11,res_json)
            if excepect_method=='json':
                excepect_dict=handJson.get_value(key,"/config/result.json")
                fag=handleResult.handle_result_json(res_dict,excepect_dict)
                if fag==True:
                    print("接口测试通过")
                    handle_excel.excel_write_data(i+1,10,"通过")
                else:
                    print("接口测试不通过")
                    handle_excel.excel_write_data(i+1,10,"失败")
                    handle_excel.excel_write_data(i+1,11,res_json)
            '''
            将数据写入Excel文件
            
            每个接口的url为key
            值为列表 ['我的_登录', '是', 'post', '', '', 'code+message', '']
          
            '''
            handle_excel.excel_write_data(i+1,1,"case"+str(i))
            handle_excel.excel_write_data(i+1,2,url_data[0])
            handle_excel.excel_write_data(i+1,3,url_data[1])
            handle_excel.excel_write_data(i+1,4,url)
            handle_excel.excel_write_data(i+1,5,url_data[2])
            handle_excel.excel_write_data(i+1,6,url_data[3])
            handle_excel.excel_write_data(i+1,7,url_data[4])
            handle_excel.excel_write_data(i+1,8,url_data[5])
            handle_excel.excel_write_data(i+1,9,url_data[6])
        self.get_cols_value()

    def get_cols_value(self):
        emailSubject="发送接口测试邮件"
        emailContent="今日接口定时任务执行完毕，请查看邮件~~~"
        file_path=base_path+"/Case/"
        file_name="case.xlsx"
        a=10
        cols_value=handle_excel.get_colsa_value(a)
        for i in cols_value:
             if i=="失败":
                self.get_post_email(emailSubject,emailContent,file_path,file_name)
    
    def get_post_email(self,emailSubject,emailContent,file_path,file_name):
        postEmail.post_email(emailSubject,emailContent,file_path,file_name)        
            


if __name__=='__main__':
    runMainJson=RunMainJson()
    runMainJson.run_case()


   




