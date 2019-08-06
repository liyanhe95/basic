#为什么要写函数
# def count_number():
#     count = 0
#     for i in range(1,100):
#         count += i
#     print('计算结果是：{}'.format(count))
#     return count  #隐式的添加
# print(count_number())
#函数里面return的表达式个数 支持0个或多个
#如果你的函数没有写return，就会隐式添加一个return 返回None
#==1 返回你指定的数据类型
#>1  返回的是元组，用逗号区分
#==0 返回None
#注意：return后面的代码不再执行，所以我们的有效代码要放在return前面
#return表示函数已经结束

# t = [2,0.09,'1',True,(1,2,3,'hello'),['python13','lemon','土豆']]
# print(t.pop(0))  #删除指定位置的函数
# print(t)
# print(t.reverse())

#1 函数的参数个数大于等于0个都行
#2 为什么要加参数，还是要提高代码的复用性
# def count_number(z,x,k):  #形参，也叫位置参数
#     count = 0
#     for i in range(z,x,k):
#         count += i
#     print('计算结果是：{}'.format(count))
#     return count  #隐式的添加
# # print(count_number(5,20,2))#实参
# # print(count_number(1,101,2))
# count_number(z=2,x=100,k=2)  #指定参数赋值
# count_number(0,101,2)

#参数类型：位置参数  默认参数  动态参数  关键字参数
#1 位置参数：是有顺序的 我们通过函数传参的时候是按顺序赋值
#2 形参 实参
#3 指定参数赋值 声明赋值 变量名要跟形参一致
#count_number(z=2,x=100)  #指定参数赋值

#默认参数：我们给形参指定一个默认值
#有实参就用实参 没有实参就用默认参数值

#注意  位置参数必须再默认参数之前
#调用函数的时候  有几个位置参数就要传几个参数  否则就会报错

#动态参数  *args 不定长参数 你想传几个就传几个  参数之间用逗号隔开
#1 可以任意传多个参数，不限制数据类型，参数之间用逗号隔开
#2 参数到了函数内部就变成了元组
#3 args  默认写这个   一定要有*号
# def robot_cat(*args):
#     print(args)

# robot_cat('20k的offer','money','女朋友','薯片',200000)
# a = ['20k的offer','money']
# b = {'name':'xiaohe','offer':'18'}
# robot_cat(a)
# robot_cat(*a)  #*可以理解为脱外套  脱外套只脱一层
# robot_cat(b)
# robot_cat(*b)

#关键字参数 **kwargs key value的形式 key word arguments
#1 key value的形式参数之间用逗号隔开
#2 参数到了内部  就变成了字典

# def anyway(**kwargs):
#     print(kwargs)
#
# anyway(x=1,b=2,c=4)  #必须是形参指定的