#coding=utf-8
import unittest
import os
import sys
import datetime
import time
import HTMLTestRunner
'''
os.getcwd()方法用于返回当前工作目录
'''
base_path=os.getcwd()
print(base_path)
sys.path.append(base_path)
from testcase.test_bookstore import TestBookStore
from testcase.test_my import TestMy
from util.post_email import postEmail
case_01=unittest.TestLoader().loadTestsFromTestCase(TestBookStore)
case_02=unittest.TestLoader().loadTestsFromTestCase(TestMy)
suite=unittest.TestSuite()
suite.addTest(case_01)
suite.addTest(case_02)
# runner=unittest.TextTestRunner()
# runner.run(suite)
'''
    生成测试报告的地址
    '''
                    
file_name='report'+str(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))+'.html'
file_path=base_path+'/report/'
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
with open(file_path + file_name,'wb') as f:
        
    runner = HTMLTestRunner.HTMLTestRunner(f, verbosity=2, title='Test', description='测试报告')
    runner.run(suite)
postEmail.post_email("发送接口测试邮件", "今日接口定时任务执行完毕，请查看邮件~~~",file_path,file_name)