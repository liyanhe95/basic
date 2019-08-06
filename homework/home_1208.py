
# 1：一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，
# 会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，
# 再显示出折扣（%10或20%）和最终价格
#写成函数  最大化复用
# def discount(min,max,discount_1,discount_2):
#     while True:
#             price = input('欢迎来到沃尔玛超市，请输入你购买商品的价格：')
#             if price.isdigit():
#                 price = int(price)
#                 if min<=price<=max:
#                     discount_1 = price*(1-discount_1/100)
#                     print('您购买的商品的总价为{}，可以享受10%的折扣，所以您购买商品的价格为{}'.format(price,discount_1))
#                 elif price>max:
#                     discount_2 = price*(1-discount_2/100)
#                     print(('您购买的商品的总价为{}，可以享受20%的折扣，所以您购买商品的价格为{}'.format(price,discount_2)))
#                 else:
#                     print('您购买商品的价格为{},谢谢光临'.format(price))
#                 break
#             else:
#                 print('请输入数字')
# discount(100,200,50,80)
# # 2、输出99乘法表
for a in range(1,10):
    for b in range(1,a+1):
        print("%d*%d=%2d" % (a, b, a*b), end=" ")
    print()

# 3、输入num为四位数，对其按照如下的规则进行加密：
# 1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2）将该数的第1位和第4为互换，第二位和第三位互换
# 3）最后合起来作为加密后的整数输出
# list = []
# number = input('请输入四位数字：')
# if number.isdigit() and len(number)==4:
#             for i in number:
#                 new_number = (int(i)+5)%10
#                 list.append(new_number)
#             list.reverse()
#             s = ''
#             for item in list:
#                 s += str(item)  #强制转换
#             print(s)
# s = [1,2,3,4]
# s[0],s[3]=s[3],s[0]
# print(s)
            # print(list)
            # new_number = 1000*int(list[0])+100*int(list[1])+10*int(list[2])+int(list[3])
            # print('加密后的数据为{}'.format(new_number))

# 4：用户的登录信息存在在字典里面，例如{" admin ":"lemon","huahua":"123456"}，
# 用户名：admin 对应密码：lemon
# 用户名：huahua对应密码：123456
# 根据上述信息以及下列条件写出符合题目的程序代码：
# 1）设计1个登陆的程序， 不同的用户名和对成密码存在个字典里面， 输入正确的用户名和密码去登陆，
# 2）首先输入用户名，如果用户名不存在或者为空，则一直提示输入正 确的用户名
# 3）当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应， 则提示密码错误请重新输入。
# 4）如果密码输入错误超过三次，中断程序运行。
# 5）当输入密码错误时，提示还有几次机会
# 6）用户名和密码都输入正确的时候，提示登陆成功!'''
# number = 0
# user_info = {'admin':'lemon','huahua':'123456'}
# while True:
#     account = input('请输入用户名:')
#     if account in user_info.keys():
#         while number<3:
#             password = input('请输入密码:')
#             if password == user_info[account]:
#                 print('登陆成功')
#                 break
#             else:
#                 number = number + 1
#                 print('密码错误,请重新输入,还有{}次机会'.format(3-number))
#     else:
#         print('请输入正确的用户名')
#         continue
#     break



