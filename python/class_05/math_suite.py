#写用例是unittest.TestCase
#收集用例是unittest.TestSuite
#执行用例的是unittest.TextTestRunner
import unittest
import HTMLTestRunnerNew
from basic.python.class_05.test_mathmethod_02 import TestAdd
from basic.python.class_05.test_mathmethod_02 import TestSub
from basic.python.class_05 import test_mathmethod_02 #模块的方式加载测试用例
#suite：集合套件  TestSuite测试套件   存储加载用例
suite = unittest.TestSuite()#对象

#方法一  加载测试用例 suite.addTest
# suite.addTest(TestAdd('test_add_two_zero')) #只能添加测试类的实例/对象


#方法2：通过测试类来进行加载
loader = unittest.TestLoader()#加载用例 #对象
# suite.addTest(loader.loadTestsFromTestCase(TestAdd)) #直接传递测试类名 #从测试类TestAdd所有以test_开头的测试用例

#方法3：通过模块去加载用例
suite.addTest(loader.loadTestsFromModule(test_mathmethod_02)) #直接传模块名

# with open('py13.txt','w',encoding='utf-8') as file:
#     #执行用例
#     runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2) #执行用例的类
#     runner.run(suite) #执行测试集里面的用例
#stream 把报告写入哪里
#descriptions
# verbosity 0 1 2
# 0只显示错误的报告
# 1显示成功和失败的
# 2写出来的测试报告是最详细的

with open('py13.html','wb') as file:#wb以二进制的文件把内容写进去
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,  #把文件写入哪里
        verbosity=2,  #报告的详细程度
        title='mathmethod',   #标题
        description='数学类测试报告',  #测试报告的描述
        tester='李艳荷' #执行测试的人
    )
    runner.run(suite)





