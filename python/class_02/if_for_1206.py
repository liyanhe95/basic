#运算符
#二的十次方  1024
#算术运算符  + - * /  %(取余运算)
# print(1+2)
# print(1*2)
# print(1-2)
# print(6%5)
#取余运算干啥？？？？判断一个数是奇数还是偶数
#赋值运算符  =  +=  -=
# a = 4#1存在内存里面    a相当于1的引用
# a+=1
# a-=4
# print(a)
#比较运算符 == >= <= !=  <  >   比较两个值是否相等    比较两个数的大小
#运算结果：布尔值   Ture  False
# print(3==4)
# print(3!=4)
# print('get'.upper()=='GET')  #python中是区分大小写的
#逻辑运算符  and  or  not   not > and >or
a = 10
b = -5
c = 0
# print(a>0 or b>0)   #或  左右两边只要有一边满足即可
# print(a>0 and b>0)  #且  左右两边同时满足才为真
# print(a>0 and b>0 and c>0)
# print(a>0 and b>0 or c>0)
# print(a>0 or b>0 or c>0)
# print(a>0 or b<0 or c==0)
#成员运算符  in  not in
#运算结果: 布尔值  True False
# str_1 = 'hello'
# print('h' in str_1)
# list = [1,'hello',999,9.09]
# print('h' in list[1])
# dict = {'name':'小CC','age':22}
# print(22 in dict)   #判断字典是根据key去判断

#明星
# A周杰伦
# B彭于宴
# C胡歌
# D华华
# E无组织人员
#分支引流的作用

#条件判断 根据条件去进行判断 进行处理
#圣诞节来了
#心仪的对象表白    A 巧克力+鲜花  B平安果

#条件语句   if ...else
#语法：
#if 条件表达式:
    #代码
#else:
    #代码
# 代码是从上往下执行的
# gift =  '鲜花'
# if gift == '巧克力':  #冒号  代表我们下面有子代码  要缩进
#     print('表白成功，明天可以去吃饭了')
# elif gift == '鲜花':
#     print('表白成功，可以去看电影')
# else:
#     print('表白失败，继续单身')

#if  elif  必须要加条件表达式  #逻辑运算  比较运算  成员运算
#else 不能加任何条件
# 什么情况才会执行 if elif  的子代码？？  只有当条件满足为True
#非0和非空的数据表示True  为0和为空的数据表示False

#只要返回值是True 或者是False  都可以作为if 或者elif 后面条件表达式

#从控制台获取一个成绩  根据成绩判断 如果>80是优秀 >70良好  >=60及格  <60不合格
#数据范围是0-100
# score = input("请输入你的成绩:")  #利用input从控制台获取数据都是字符串类型的
# if 80<score<=100:
#     print('成绩优秀')
# elif score>70 and score<=80:
#     print('成绩良好')
# elif score>=60 and score<=70:
#     print('成绩及格')
# elif score>100 or score<0:
#     print('数据范围在0-100之间')
# else:
#     print('成绩不合格')

# if score.isdigit():
#     score = int(score)
#     if score>100 or score<0:
#         print('数据范围在0-100之间')
#     elif score>80:
#         print('成绩优秀')
#     elif score>70 and score<=80:
#         print('成绩良好')
#     elif score>=60 and score<=70:
#         print('成绩及格')
#     else:
#         print('成绩不合格')
# else:
#     print('数据输入有误')

s = 'python13'#8
L = [1,0.2,'桃子','旅行者','向阳']#8
d = {'name':'pitt','age':18,'money':'10w'}#3
t = (1,5,6,'hello','how are you')#5
#for 循环
#什么是循环
# for item in s:#利用for循环  依次访问s里面的每一个元素  赋值给item这个变量
#     print(item)

#1:是不是可以访问指定的数据里面的元素
#2:利用遍历去控制循环字数

#练习题
#请利用for循环  依次打印d里面的value
# for i in d:
#     i = d.values()
#     print(i)
#
# for i in d:
#     print(d.values())

# for i in d:
#     print(d[i])
# for i in d.values():
#     print(i)
#循环的字数由元素的长度决定
p = [[1,2,3],[4,5,6],[7,8,9]]
#请访问p里面的子列表里面的每个元素  并且打印出来
for i in p:  #嵌套循环的由来
    for a in i:
        print(a)