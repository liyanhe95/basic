#unittest 类  专门写用例的
#TestCase类 专门写用例的
#TestCase 里面初始化函数的methodname 指的是每一条用例的方法名
import unittest
from basic.python.class_05.class_mathmethod_02 import MathMethod
from basic.python.class_05.do_excel_math import DoExcel
class TestAdd(unittest.TestCase):#继承
    #两个0相加 两个负数相加 一正一负相加
    #用例的写法：每一条用例就是一个方法 def test_用例描述(self)
    #必须是test_开头
    #超继承
    def __init__(self,case_id,title,a,b,excepted,methodName):#override
        #超继承  既有子类的方法，也会执行父类的方法
        super(TestAdd,self).__init__(methodName) #关键的就在这 ，调用父类的init方法
        self.case_id = case_id
        self.title = title
        self.a = a
        self.b = b
        self.excepted = excepted

    def setUp(self):  #重写  #初始化测试环境   #执行每一条用例的时候都会执行
        self.excel = DoExcel('python13.xlsx','add')#创建的对象
        print('开始执行第几条{}用例{}'.format(self.case_id,self.title))

    def tearDown(self): #重写
        print('用例执行完毕')
    def test_add(self): #两个0相加
        result = MathMethod().add(self.a,self.b)
        try:
            self.assertEqual(self.excepted, result)
            testresult = 'pass' #如果代码进入try，那么用例通过
        except AssertionError as e:
            testresult = 'failed'#如果代码进入到except了里面，用例就不通过
            print('断言出错：{}'.format(e)) #断言 判断期望结果和实际结果是否一致
            raise e

        finally:
            #写回结果
            self.excel.write_back(self.case_id+1,6,result)#写回测试的实际结果
            self.excel.write_back(self.case_id+1,7,testresult)#写回测试结论，到底是通过还是不通过


    def test_add_two_nagetive(self):#两个负数相加
        result = MathMethod().add(self.a,self.b)
        try:
            self.assertEqual(self.excepted, result)
        except AssertionError as e:
            print('断言出错：{}'.format(e))
            #抛出异常
            raise e
        print('两个负数相加的结果是{}'.format(result))

    def test_add_positive_nagetive(self):#一正一负相加
        result = MathMethod().add(self.a,self.b)
        try:
            self.assertEqual(self.excepted, result)
        except AssertionError as e:
            print('断言出错：{}'.format(e))
            raise e
        print('一正一负相加的结果是{}'.format(result))

class TestSub(unittest.TestCase):
    def setUp(self):  #重写  #初始化测试环境   #执行每一条用例的时候都会执行
        self.test_data = [[5,2],[-5,-2],[-9,-3]]
        print('开始执行用例')

    def tearDown(self): #重写
        print('用例执行完毕')

    def test_sub_two_zheng(self):#两个正数相减
        result = MathMethod().sub(self.test_data[0][0],self.test_data[0][1])
        excepted = 3
        try:
            self.assertEqual(result,excepted)
        except AssertionError as e:
            print('断言出错：{}'.format(e))
            raise e
        print('两个正数相减的结果是{}'.format(result))

    def test_sub_two_nagetive(self):#两个负数相减
        result = MathMethod().sub(self.test_data[1][0],self.test_data[1][1])
        excepted = -3
        try:
            self.assertEqual(excepted,result)
        except AssertionError as e:
            print('断言出错：{}'.format(e))
            raise e
        print('两个负数相减的结果是{}'.format(result))

    def test_sub_two_positive_nagetive(self):#一正一负相减
        result = MathMethod().sub(self.test_data[2][0],self.test_data[2][1])
        excepted = -6
        try:
            self.assertEqual(excepted,result)
        except AssertionError as e:
            print('断言出错：{}'.format(e))
            raise e
        print('一正一负相减的结果是{}'.format(result))

class TestA_b_s(unittest.TestCase):
    def setUp(self):  #重写  #初始化测试环境   #执行每一条用例的时候都会执行
        self.test_data = [[5,4],[-9,-1],[2,-7]]
        print('开始执行用例')

    def tearDown(self): #重写
        print('用例执行完毕')

    def test_abs_two(self):#两个正数的绝对值
        result = MathMethod().a_b_s(self.test_data[0][0],self.test_data[0][1])
        excepted = 1
        try:
            self.assertEqual(excepted,result)
        except AssertionError as e:
            print('断言出错：{}'.format(e))
            raise e
        print('两个正数的绝对值是{}'.format(result))

    def test_abs_two__nagetive(self):#两个负数的绝对值
        result = MathMethod().a_b_s(self.test_data[1][0],self.test_data[1][1])
        excepted = 8
        try:
            self.assertEqual(excepted,result)
        except AssertionError as e:
            print('断言出错：{}'.format(e))
            raise e
        print('两个负数的绝对值是{}'.format(result))

    def test_abs_two_positive_nagetive(self):#一正一负数的绝对值
        result = MathMethod().a_b_s(self.test_data[2][0],self.test_data[2][1])
        excepted = 9
        try:
            self.assertEqual(excepted,result)
        except AssertionError as e:
            print('断言出错：{}'.format(e))
            raise e
        print('一正一负数的绝对值是{}'.format(result))

#用例执行的顺序与ASCII编码有关
#zero 3
#nagetive 2
#positive_nagetive 1
#减法3条 ，绝对值写3条，加好断言

if __name__ == '__main__':
    unittest.main()#会自动在当前文件里面加载test_开头的用例




















