# 1：写一段程序，分别求出0-100之间的所有偶数的和和所有奇数的和。
# sum = 0  #初始值  用来存储奇数和
# for i in range(1,101,2):  # 1 3 5 7 9
#     sum = sum + i
# print('奇数和：',sum)
# num = 0  #初始值  用来存储偶数和
# for a in range(0,102,2): # 0 2 4 6 8
#     num = num + a
# print('偶数和：',num)

#方法2：
sum_1 = 0 #初始值  用来存储奇数和
sum_2 = 0 #初始值  用来存储偶数和
for item in range(101):
    if item%2 == 0:
        sum_2 = sum_2 + item
    else:
        sum_1 = sum_1 + item
print('奇数和：',sum_1)
print('偶数和：',sum_2)
# 2：一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
# d = {'m': '男性', 'f': '女性'}
# num = 0  #记录满足条件的人数
# for item in range(1, 11):
#     sex = input('请输入性别：m表示男性，f表示女性')
#     # sex = d[sex]
#     if sex == 'f':
#         age = input('请问你的年龄是：')
#         if age.isdigit():
#             age = int(age)
#             if 10 <= age <= 12:
#                 num = num + 1
#                 print('恭喜您可以加入我们的女子足球队了！！！')
#             else:
#                 print('对不起你的年龄没达到我们的要求！')
#     else:
#         print('对不起我们这里是女子足球队！！！')
# print('满足条件的总人数:{}'.format(num))

count = 0
while count<10:
    count = count + 1
    sex = input('请输入性别：m表示男性，f表示女性')
    if sex == 'f':
        age = input('请问你的年龄是：')
        if age.isdigit():
            age = int(age)
            if 10 <= age <= 12:
                print('恭喜您可以加入我们的女子足球队了！！！')
                continue
            else:
                print('对不起你的年龄没达到我们的要求！')
    else:
        print('对不起我们这里是女子足球队！！！')
print('满足条件的总人数:{}'.format(count))

# dict={'m':'男性','f':'女性'}
# c=0
# for item in range(1,11):
#     sex = input('请问你的性别是：')
#     age = int(input('请输入你的年龄：'))
#     if sex=='女性' :
#         c=c+1
#         print(c)
#     else:
#         print('对不起你的年龄不符合要求！')
# 3：请输出如下直角三角形：
# *
# **
# ***
# ****
# *****
xing = '*'

# for i in xing:
#     print(i)
#     for i in xing:
#         print(i*2)
#         for i in xing:
#             print(i*3)
#             for i in xing:
#                 print(i*4)
#                 for i in xing:
#                     print(i*5)
#
# for i in range(5): # 0 1 2 3 4
#     a = '*'*(i+1)
#     print(a)
# for i in range(1,6): #i=1 i=2
#     for j in range(1,i+1):#range(1,2)
#         print('*',end = '')
#     print()

# for i in range(1,6):
#     print(i*'*',end = '')
#     print()
# print()  起到换行的作用
# end = '' 阻止换行的作用
