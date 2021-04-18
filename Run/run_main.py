#coding=utf-8
import sys
import os
import json
base_path=os.getcwd()
sys.path.append(base_path)
#from handle.handle_excel import HandExcel
from handle.handle_excel import handle_excel
from Base.base_request import request_base
from handle.handle_ini import handleIni
from handle.handle_result import handleResult
from util.post_email import postEmail

class RunMain:
    def __init__(self):
        self.host_server=handleIni.get_value('host')
        pass
    '''
    ['case001', '我的_登录', '是', '/dj_user/out/login/loginByPhoneV2?usr=j27871222&rgt=7&p1=V3WygQ4dlCADADL64yvBGhkY&pc=10&p2=124011&p3=17126056&p4=501656&p5=12&p6=&p7=__3e932cc0f202a00f&p9=2&p12=&p16=vivo+Y51A&p21=3&p22=5.1.1&p25=17126056&p26=22 HTTP/1.1', 'post', None, None, 'code+message', None, None, None]
    '''
    def get_post_email(self,emailSubject,emailContent,file_path,file_name):
        postEmail.post_email(emailSubject,emailContent,file_path,file_name)

    def run_case(self):
        max_rows=handle_excel.get_rows()
        for i in range(max_rows-1):
            # print(handle_excel.get_rows_value(i+2))
            data_value=handle_excel.get_rows_value(i+2)
            method=data_value[4]
            data=data_value[5]
            excepect_method=data_value[7]
            if i==3:
                url=data_value[3]
                res=request_base.send_method(method,url,data)
                res1=json.loads(res)
            else:
                url=self.host_server+data_value[3]
                # print(request_base.send_method(method,url,data))
                res=request_base.send_method(method,url,data)
                res1=json.loads(res)
                '''
                将通过实际的url/code 对应的msg 与接口文档中的（即code_message.json文件中的 url/code 对应的message是否一致来定测试是否通过）
                '''
                code=str(res1.get("code"))
                msg=res1["msg"]
                message=handleResult.get_value(data_value[3],code)
                print(len(msg),message,'================================>')
            if excepect_method=="code+message":
                if message==msg:
                    print("接口测试通过")
                    handle_excel.excel_write_data(i+2,10,"通过")
                else:
                    print("接口测试不通过")
                    handle_excel.excel_write_data(i+2,10,"失败")
                    handle_excel.excel_write_data(i+2,11,res)
                print('已成功执行1个接口测试代码code+message')
            elif excepect_method=="code":
                print(data_value[8])
                if data_value[8]==code:
                    print("接口测试通过")
                    handle_excel.excel_write_data(i+2,10,"通过")
                else:
                    print("接口测试不通过")
                    handle_excel.excel_write_data(i+2,10,"失败")
                    handle_excel.excel_write_data(i+2,11,res)
                print('已成功执行1个接口测试代码code')
            else:
                excepect_result_json=handleResult.get_result_json(data_value[3])
                fag=handleResult.handle_result_json(res1,excepect_result_json)
                if fag==True:
                    print("接口测试通过")
                    handle_excel.excel_write_data(i+2,10,"通过")
                else:
                    print("接口测试不通过")
                    handle_excel.excel_write_data(i+2,10,"失败")
                    handle_excel.excel_write_data(i+2,11,res)
                print('已成功执行1个接口测试代码JSON')
        emailSubject="发送接口测试邮件"
        emailContent="今日接口定时任务执行完毕，请查看邮件~~~"
        file_path=base_path+"/Case/"
        file_name="case.xlsx"
        self.get_post_email(emailSubject,emailContent,file_path,file_name)
            


             
        

if __name__=='__main__':
    runMain=RunMain()
    runMain.run_case()