import unittest
import HTMLTestRunnerNew
from basic.python.class_05 import test_jd

suite = unittest.TestSuite() #收集测试用例
loader = unittest.TestLoader()#加载用例 #对象
#方法3：通过模块去加载用例
suite.addTest(loader.loadTestsFromModule(test_jd)) #直接传模块名

with open('jd.txt','w',encoding='utf-8') as file:
    #执行用例
    runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2) #执行用例的类
    runner.run(suite) #执行测试集里面的用例

# with open('jd.html','wb') as file:#wb以二进制的文件把内容写进去
#     runner = HTMLTestRunnerNew.HTMLTestRunner(
#         stream=file,  #把文件写入哪里
#         verbosity=2,  #报告的详细程度
#         title='mathmethod',   #标题
#         description='数学类测试报告',  #测试报告的描述
#         tester='李艳荷' #执行测试的人
#     )
#     runner.run(suite)

