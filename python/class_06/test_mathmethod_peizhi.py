#unittest 类  专门写用例的
#TestCase类 专门写用例的
#TestCase 里面初始化函数的methodname 指的是每一条用例的方法名
import unittest
from ddt import ddt,data
from basic.python.class_06.my_log import MyLog
from basic.python.class_06.class_mathmethod_02 import MathMethod
from basic.python.class_06.do_excel_manth_peizhi import DoExcel
#unpack 拆分，把data解包的数据，再次根据逗号去拆分，有几个变量，测试方法就要用几个变量来接收值
#unpack 如果unpack的对象是字典，那么下面接收参数的变量必须要与key的值一致
cases = DoExcel('python13.xlsx', 'add').get_data()  # 嵌套列表
my_logger = MyLog()#创建的日志对象
@ddt#@符号是装饰器的符号（装饰的是测试类，只有继承TestCase的时候才叫测试类）
class TestAdd(unittest.TestCase):#继承
    #两个0相加 两个负数相加 一正一负相加

    def setUp(self):  #重写  #初始化测试环境   #执行每一条用例的时候都会执行
        self.excel = DoExcel('python13.xlsx','add')#创建的对象
        my_logger.info('开始执行用例')

    def tearDown(self): #重写
        my_logger.info('用例执行完毕')

    @data(*cases) #装饰我们的测试方法  #传进来的是列表，加一个星号进行解包
    def test_add(self,item): #测试方法用一个变量case来接收我们data传递的数据

        print(item)
        # a=item.__dict__ #可以查看对象里面的东西
        my_logger.info('开始执行第{}条用例：{}'.format(item.id,item.title))
        result = MathMethod().add(item.a,item.b)
        try:
            self.assertEqual(item.excepted, result)
            TestResult = 'pass' #如果代码进入try，那么用例通过
        except AssertionError as e:
            TestResult = 'failed'#如果代码进入到except了里面，用例就不通过
            my_logger.error('断言出错：{}'.format(e)) #断言 判断期望结果和实际结果是否一致
            raise e

        finally:
            #写回结果
            self.excel.write_back(item.id+1,6,result)#写回测试的实际结果
            self.excel.write_back(item.id+1,7, TestResult)#写回测试结论，到底是通过还是不通过



#用例执行的顺序与ASCII编码有关
#zero 3
#nagetive 2
#positive_nagetive 1
#减法3条 ，绝对值写3条，加好断言

if __name__ == '__main__':
    unittest.main()#会自动在当前文件里面加载test_开头的用例




















