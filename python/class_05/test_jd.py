import unittest
from basic.python.class_05.jd_01 import Jd

class TestJd(unittest.TestCase):

    #编写京东类的测试用例
    def test_count_sucess(self):
        result = Jd('京东','电子产品','刘强东','自营').count()
        excepted = range(10,51)
        try:
            self.assertIn(result,excepted)
        except ArithmeticError as e:
            print('断言错误{}'.format(e))
            raise e
        print()


if __name__ == '__main__':
    unittest.main()#会自动在当前文件里面加载test_开头的用例

