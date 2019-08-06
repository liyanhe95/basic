#-*- coding:utf-8
#@time:2019/4/14
#@author:李艳荷
#@Email:976621712
#@File:varibale
#@Software:PyCharm
#变量
# x = 1
# y = x * 5 #x是变量  y是因变量
"""
变量名：我们命名一个标识符存储一个数据
数据：数字 字符串 列表 元组 字典 集合等各种数据类型
常量就是程序运行过程中，值不能改变的量，比如pi 身份证号
"""
# a = 1
# b = 1
#内置函数id() 获取变量的内存地址
# print(id(a))  #id 读取内存地址
# print(id(b))  #指向的是同一个内存地址

"""
python 的数据类型
数字:
int (有符号整型)
float（浮点型）
type() 判断数据类型的函数
"""
# x = 10
# print(type(x))
# print(type(10.00))
"""
字符串 str  string
成对的单引号 双引号 以及三引号括起来的内容都是字符串
c = '10'
d = "hello"
在python中，单引号和双引号没有区别，都是表示字符串
如果字符串必须包含单引号  最外层用双引号
如果字符串必须包含双引号  最外层用单引号
字符串里面的元素：单个字符算一个元素（数字 字母 符号 中文）
统计数据的长度 len()
如何取值:字符串取值是根据索引取值
索引是字符串元素的编号   编号是从0开始
切片：字符串的用法  变量名[m:n:k]  取头不取尾（取左不取右，取到 n-1）
m:开始取值的索引位置  n:结束取值的索引位置  k:步长   
::  表示从头取到尾
"""
# x = '''"hello"'''
# print(x)
a = 'hello python13'
# print(len(a))
# print(a[-1])
# print(a[13])
# print(a[6])
# print(a[0:13:1])  # 0 1 2 3 4 5 6 7 8 9 10 11 12
# print(a[0:13:3])  # 0 3 6 9 12
#请把a字符串编号为偶数的打印出来
# print(a[0:13:2])
# print(a[::2])
# 请把a字符串利用切片实现倒序输出
# print(a[::-1])
# print(a[13::-1])  # 13 12 11 10 9 8 7 6 5 4 3 2 1 0
# height = float(input('请输入您的身高：'))
# weight = float(input ('请输入您的体重：'))
# bmi = weight/(height*height)
# if bmi < 18.5:
#     print('您的体重过轻')
# elif bmi >= 18.5 and bmi<24.9:
#     print('正常范围，请注意保持')
# elif bmi > 29.9:
#     print('肥胖')
#字符串的拼接
# s_1 = 'hello'
# s_2 = 'word'
# print(s_1 +  s_2)
#格式化输出   占坑符  %d 数字  %f 浮点数  %s 字符串   万能的是%s
#%f 精确到小数点后6位
age = 22
height = 1.53
hobby = '看书'
# print('''-----小呵呵的个人绝密档案-------
#       年龄是：%d
#       身高是：%0.2f   #在小数点后面保留两位数
#       业余爱好：%s'''%(age,height,hobby))

# print('''-------max的个人绝密档案-------
#       年龄是：{}
#       身高是：{}
#       业余爱好：{}'''.format(age,height,hobby))
#函数
a = 'hEllo pYthOn13'
#切换大小写(仅仅用于字符串)  面试题
print(a.upper())
# print(a.lower())
#大小写互换
# print(a.swapcase())
#固定某个字母的大小写
s = ""
#指定转换某个字符的大写或小写
# for i in range(len(a)):
#     if i == 7:
#         s += a[i].lower()
#     else:
#         s += a[i]
# print(s)
# for i in range(len(a)):

#替换
# s = a.replace('n','N')
# s = a.replace('l','o',1)
# print(s)
#指定替换某个字符串用for循环
# for i in range(len(a)):
#     if i == 3:
#         s += a[i].replace('l','o')
#     else:
#         s += a[i]
# print(s)

#面试题必备
#将字符的大小写互换
# a = 'hEllo pYthOn13'
# b = ""
# for i in a:
#     if 'a'<= i <='z':
#         b += i.upper()
#     elif 'A' <= i <= 'Z':
#         b += i.lower()
#     else:
#         b += i
# print(b)

#find  查找元素(根据字符串去查找，如果找到了，返回的是索引的值，
# 没有找到返回-1)
# print(a.find('l'))#单个字符如果找到了，返回的是遇到第一个元素的索引值
# print(a.find('hEllo'))  #子字符串   长度大于1  如果找到了就返回字符串里面第一个元素的位置
# print(a.find('13'))
#
# print(a.capitalize())  #首字母大写
# print(a.count('l'))   #计算字符在字符串中出现的字数
# print(a.index('3'))   #查找元素的索引，只会查找在字符串中第一次遇到的元素
# print(a.isdigit())  #判断元素是否是数字

#布尔值  Ture False
# b = '1'  #b的类型是字符串，但是isdigit判断里面是数字
# print(b.isdigit())
# #判断字母是大写还是小写  isupper  islower
# print(a[1].isupper())
# print(a[0].islower())
# print(a.split(' '))  #切割   根据空格去切割   返回的是列表
# print(a.split('l'))
#切片和切割的区别
#切割返回的是列表，切片返回的是字符串