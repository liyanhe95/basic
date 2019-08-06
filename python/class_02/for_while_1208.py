#for循环    有限次数的循环
#for 循环的作用
#1 遍历元素
#2 可以控制循环次数
# for循环可遍历的数据类型:str tuple list dict......,只要是可迭代的，就可以用for循环来遍历
# 如果用整数:TypeError: 'int' object is not iterable
#可迭代的数据类型：数据里面允许存在多个元素的
# for item in 5:
#     print(item)
# 想办法：怎么利用函数去判断我的数据类型是可迭代的
# d = {'name':'pitt','age':18,'money':'10w'}#3
# a = 0
# for item in d.values():  #字典是无序的，所以打印出来不是固定的
#     a+=1
#     print('这是第{}次循环'.format(a))
#     print(item)
#range 函数:生成一个整数序列  可迭代对象
#range(m,n,k)  m开头的数字 n结尾的数字 k步长,默认值为1  取左不取右
#如果range(m,n)  k默认为1
#如果range(n)    m默认为0
# for item in range(1,10,3):  #1 4 7
#     print(item)
#题目我要生成0-100的数字
# for item in range(0,101):
#     print(item)
#嵌套循环 ：循环里面还有循环
# p = [[1,2,3],[4,5,6],[7,8,9]]
# for a in p:  #外层循环
#     for b in a: #内层循环
#         print(b)
#while循环  可以无限次数循环(死循环)  同时加以好好利用  用条件   有条件控制的循环
#wheile 循环语法
#while 条件表达式:
    #循环体

#条件表达式: 跟if一样
#1 一般逻辑运算 比较运算 成员运算
#2 非0和非空的数据表示True 为0和为空的数据表示False(非常重要)
#3 可以直接用布尔值来代替表达式

#运行模式:先判断while后面的条件 满足就执行循环体 不满足就不执行
#执行完毕之后 再次判断while后面的条件 满足就执行循环体 不满足就不执行
#如此反复
#怎么达到不是绝对的True 也不是绝对的False
#1：基本解决方法：break 中止循环 如果用的不好的话  就是执行一次
#2：进阶使用：break + 条件 条件是你规定它循环多少次
#3: 高级使用：必要的时候 脱离break  自由自在
# a = 0
# while True:
#     a += 1
#     print('a的值',a)
#     if a == 10:
#         break
#     print('我是一个死循环{}'.format(a))

#高级使用
a = 0
while a<10:
    a += 1
    print('a的值',a)
    print('我是一个死循环{}'.format(a))