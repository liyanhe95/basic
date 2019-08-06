#写用例是unittest.TestCase
#收集用例是unittest.TestSuite
#执行用例的是unittest.TextTestRunner
import unittest
import HTMLTestRunnerNew
from basic.python.class_05.do_excel_math import DoExcel
from basic.python.class_05.test_mathmethod_02 import TestAdd
from basic.python.class_05.test_mathmethod_02 import TestSub

#suite：集合套件  TestSuite测试套件   存储加载用例
suite = unittest.TestSuite()#对象
cases =DoExcel('python13.xlsx','add').get_data()
for case in cases:
    suite.addTest(TestAdd(case.id,case.title,case.a,case.b,case.excepted,'test_add'))


with open('py13.html','wb') as file:#wb以二进制的文件把内容写进去
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,  #把文件写入哪里
        verbosity=2,  #报告的详细程度
        title='mathmethod',   #标题
        description='数学类测试报告',  #测试报告的描述
        tester='李艳荷' #执行测试的人
    )
    runner.run(suite)





