#1.编写一个名为make_shirt的函数，它接受一个尺码以及要打印到T恤上的字样。
# 这个函数打印一个句子，概要的说明T恤的尺码和字样
#L表示大号T恤   M表示中号  S表示小号
# def make_shirt(size,text):
#     print('你选择的T恤是{}码，字样是{}'.format(size,text))
#
# make_shirt('S','致我们的青春')

#2.编写一个名为describe_city()的函数，他接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，
# 如reykjavik is in lceland 。给用于存储国家的形参指定默认参数。为三座不同的城市调用这个函数，且其中至少有一
#座城市不属于默认国家

# def describe_city(city,country='China'):
#     print('{}is in {}'.format(city,country))
#
# describe_city('beijing')
# describe_city('shanghai')
# describe_city('Japan','Tokyo')

# 3.编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。
#这个函数应返回一个格式类似于下面的字符串：
#“长沙，中国”
#至少使用三个城市国家调用这个函数，并打印它返回的值
#
# def city_country(city,country):
#     print('“{},{}”'.format(city,country))
#
# city_country('北京','中国')
# city_country('日本','东京')
# city_country('巴黎','法国')

#4、编写一个命名为make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，
#并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字
#典正确地存储了专辑的信息
def make_album(**kwargs):
    return kwargs

print(make_album(singer='陈小春',song='独家记忆'))
print(make_album(singer='张杰',song='我们不一样'))
print(make_album(singer='筷子兄弟',song='父亲'))


#5.编写一个函数，它接受顾客要在三明治中添加的一系列食材，这个函数只有一个形参（它收集函数调用中提供的所有食材）
#并打印一条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提高不同数量的实参。
# def food(*args):
#     print('欢迎来到汉堡王：',args)
#
# food('火腿三明治')
# food('鸡蛋三明治')
# food('巧克力三明治')

#1.定义一个函数，成绩作为参数传入。如果成绩小于60，则输出不及格。如果成绩在60-80之间，则输出良好；如果成绩高于80分，
#则输出优秀，如果成绩不在0-100之间，则输出成绩输入错误。
#isdigit（）是字符串的属性 不是int的attribute（属性）
# def subject_score():
#     while 1==1:
#         socre = input('请输入你的成绩：')
#         if socre.isdigit():
#             socre = int(socre)
#             if socre<0 and socre>100:
#                 print('成绩录入错误')
#             elif socre<60:
#                 print('成绩不及格')
#             elif 60<=socre<=80:
#                 print('成绩优秀')
#         else:
#             print('请输入数字')
#             continue
#         break
#
# subject_score()

#2、用函数实现
#企业发放的奖金根据利润提成。
#利润（I）低于或等于10万时，奖金可提10%；
#利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
#20万元到40万元之间时，高于20万元的部分，可提成5%；
#40万元到60万元之间时，高于40万元的部分，可提成3%；
#60万元到100万元之间时，高于60万元的部分，可提成1.5%，高于100万元时，超高100万元的部分按1%提成
#从键盘输入当月利润I，求应发放奖金总数？

# def bonus():
#     while 1==1:
#         profit = input('请输入你当月的利润：')
#         if profit.isdigit():
#             profit = int(profit)
#             if profit <= 10:
#                 print('你的奖金低于或等于10万时，奖金可提10% {} '.format(profit*1.1),end="")
#             elif 10<profit<=20:
#                 print('你的奖金在10-20万之间，低于10万元的部分按10%提成，高于10万元的部分可提成7.5% {} '.format(11 + (profit - 10) * 1.075), end=" ")
#             elif 20<profit<=40:
#                 print('20万元到40万元之间时，高于20万元的部分，可提成5% {} '.format(21.75 + (profit- 20) * 1.05), end=" ")
#             elif 40<profit<=60:
#                 print('40万元到60万元之间时，高于40万元的部分，可提成3% {} '.format(42.75 + (profit - 40) * 1.03), end=" ")
#             elif 60<profit<=100:
#                 print('60万元到100万元之间时，高于60万元的部分，可提成1.5% {} '.format(63.35 + (profit - 60) * 1.015), end=" ")
#             else:
#                 print('高于100万元时，超高100万元的部分按1%提成 {} '.format(103.95 + (profit - 100) * 1.01), end=" ")
#         else:
#             print('输入有误，请重新输入')
#             continue
#         break
#
# bonus()

#3、随机产生一个数，让用户猜，猜中结束，若猜错，则提示用户猜大或猜小
# import random
# shu = random.randint



#4.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
#5、写函数，将姓名、性别、城市作为参数，并且性别默认为f（女）。如果城市是在长沙并且性别为女，则输出姓名、性别、城市，
# 并返回Ture，否则返回False
#6、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，
#并将新的内容返回
#7、定义一个函数，传入一个字典和字符串，
# 判断字符串是否为字典中的值，如果字符串不在字典中，
#则添加到字典中，并返回新的字典

# import random
# #random 生成随机整数  随机字符串  ''.join的用法
# def random_key(d):
#     sui = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz',3))#生成随机三个长度的字符串
#     while sui in d.keys():
#         sui = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz',3))
#     return sui
# def add_str_to_dict(d,string):
#     if s not in d.values():
#         if s not in d.keys():
#             d[string] = string
#         else:
#             key = random_key(d)
#             d[key]=string
#     print(d)

# d = {'hello': 'huahua'}
# s = 'hello'
# add_str_to_dict(d,s)

#1、有1.2.3.4个数字 ，能组成多少个互不相同且无重复数字的三位数？都是多少？
#百十个
#1 2 3 4
#4*3*2=24
# a  #代表百位
# b   #代表十位
# c   #代表各位
# def generate_num():
#     count = 0 #记录满足条件的字数
#     L = []
#     for a in range(1,5):
#         for b in range(1,5):
#             for c in range(1,5):
#                 if a!=b and b!=c and c!=a:
#                     count += 1
#                     L.append(a*100+b*10+c)
#                     print(a*100+b*10+c)
#
#     print('满足条件的次数个数：{}'.format(count))
#     print(L)
#
# generate_num()
#2.一个足球队在寻找年龄在m岁到n岁的男生or女生（包括m岁和n岁，到底是找男生还是女生，可指定性别）加入。
#编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，然后显示一条消息出这个人是否可以加入球队，