#coding=utf-8
import unittest
import os
import sys
import time
import HTMLTestRunner
base_path=os.getcwd()
sys.path.append(base_path)
from mock.test_floating import TestFloating
from mock.test_push import TestPush
case_01=unittest.TestLoader().loadTestsFromTestCase(TestFloating)
case_02=unittest.TestLoader().loadTestsFromTestCase(TestPush)
suite=unittest.TestSuite()
suite.addTest(case_01)
suite.addTest(case_02)
# runner=unittest.TextTestRunner()
# runner.run(suite)
'''
    生成测试报告的地址
    '''
file_path=base_path+'/report/report'+str(time.time())+'.html'
with open(file_path,'wb') as f:
        
    runner = HTMLTestRunner.HTMLTestRunner(f, verbosity=2, title='Test', description='测试报告')
    runner.run(suite)
#postEmail.post_email()