#单元测试
#数学类
class MathMethod:
    #这是一个数学类
    # def __init__(self,a,b):
    #     self.a = a
    #     self.b = b

    def add(self,a,b):#加法
        return a + b

    def sub(self,a,b):#减法
        return a - b

    def a_b_s(self,a,b):#返回差的绝对值
        return abs( a - b)

#调用方法  传参  观察结果==期望结果  一致 PASS  不一致Failed

#unittest pytest、
#测试用例 序号 步骤 参数 期望结果
#执行用例 对比实际结果与期望结果  pass failed
#生成测试报告

