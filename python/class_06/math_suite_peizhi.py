#写用例是unittest.TestCase
#收集用例是unittest.TestSuite
#执行用例的是unittest.TextTestRunner
import unittest
import HTMLTestRunnerNew
from basic.python.class_06.test_mathmethod_peizhi import TestAdd


#suite：集合套件  TestSuite测试套件   存储加载用例
suite = unittest.TestSuite()#对象

#loader 加载方式
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestAdd))

with open('py13peizhi.html','wb') as file:#wb以二进制的文件把内容写进去
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,  #把文件写入哪里
        verbosity=2,  #报告的详细程度
        title='mathmethod',   #标题
        description='数学类测试报告',  #测试报告的描述
        tester='李艳荷' #执行测试的人
    )
    runner.run(suite)





