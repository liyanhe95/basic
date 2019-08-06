#整数  浮点数  字符串  布尔值   （Ture False）
#元组   关键字   tuple  符号()  所有的符号都是英文状态下的符号
#1: 特征
#>圆括号括起来的数据，都是元组  type()  查看数据类型
#>空元组
#>如果一个元组里边只有一个元素，要在元素后面加一个逗号
#>元组里面可以包含各种类型的数据  整数  浮点数  元组  字符串
tuple=(2,0.089,'1',True,(1,2,3,'hello'))
print(len(tuple))
#>取值方式：与字符串一样  根据索引取值  可以切片取值
#>取单个值的方式  元组名[索引值]  索引值从0开始数
print(tuple[1])
#嵌套取值  怎么取  剥杨葱  一片一片往里剥开
s=tuple[-1]  #取出值  存到s变量里面
print(s[0])
print(tuple[-1][-1]) #快捷方式取值
print(tuple[-1][-1][-1])
#切片 ：同字符串  元组名[索引开始值:索引结束值:步长]
#取左不取右
#把索引值为偶数的打印出来
print(tuple[::2])  #从负无穷取到正无穷   步长为2
print(tuple[0:5:2])  #0 2 4
print(tuple[:5:2])
#>元组是有序数据，但是不可以做增删改
print(tuple.index(2))  #查找元素的索引
#2: 用法  和场景
#用在怎么场景下？-----心随我动


#列表 关键字  list  符号[]
#特征
#中括号括起来的数据都是列表
#空列表  t = []
#列表里面可以包含各种类型的数据 整数  浮点数   字符串 布尔值   True  False  元组   列表
#元素和元素之间用逗号隔开，看元素的长度  len
# #取单个值的方式   列表名[索引值]   索引值才0开始数
# t = [1]
# print(type(t))
# list = [2,0.089,'1',True,(1,2,3,'hello'),['python','lemon','土豆','西红柿']]
# print(list)
# print(len(list))
# print(list[4][2])
# print(list[-2][-2])
# print(list[5][2])
# print(list[-1][-2])
#切片：同字符串、元组  列表名[索引开始值:索引结束值:步长]
#取左不取右
#请把最后一个嵌套列表的索引为偶数的值打印出来
# print(list[5][::2])
# print(list[-1][::2])
#列表是有序数据 支持增删改
# print(list.index(2))
# print(list.count(True))
# t = list.clear()
# print(t)

#用在什么场景呢
#增加
#1加在尾部  列表名.append(value)   一次只能增加一个元素
# list.append('不加糖的咖啡')
# print(list)
#2在指定的索引位置加元素  列表名.insert(i,value)
# list.insert(0,'向阳同学')
# print(list)
#添加列表   列表名.extend(第二个列表名) 合并列表
# list1=['海绵','磐石','monkey','ing']
# list.extend(list1)
# print(list)
#或者   list+list1   这种方式不推荐
#删除
#1：删除最后一个元素    列表名.pop()
# list.pop()
# print(list)
#2：删除指定索引位置的一个元素  列表名.pop(i)
# list.pop(0)
# print(list)
# #reverse()  反向列表中的元素
# list.reverse()
# print(list)
#sort()  对原列表进行排序  数字之间进行排序    同类型的进行排序   字符串没有排序的必要
a = [9,1,0,4,3,6,8]
# a.sort()
# print(a)
# a.sort(reverse=True)   #从大到小排序
# print(a)
#修改元素的值   重新赋值
# list[-1][-1]='shaw'
# print(list)
#列表可以删除和元组可以删除是绝对的？  ----不是绝对的
#注 元组是不可以修改的   但是列表里面的整个元组可以被替换（元组的保护性特强）
# list[4]='柠檬'
# print(list)
# t = (2,0.089,'2',(1,2,3,'word'),2,3,468,['不将就','sunny','土豆'])
# t[-1]='9'  #元组里面的元素是不支持增删改
# t[-1][-1]='爱飞的鱼'
# print(t)
#为啥有的数据可以直接输出  有的数据不可以直接输出
# print(list.index(2))
# print(list.reverse())
# a.reverse()
# print(a) 函数以及函数的返回值

#字典   关键字    dict  dictionary
#特征
#花括号括起来的数据都是字典   在英文状态下输入
#空字典  dict = {}
#字典里面元素存储的方式是 key:value的形式  键值对
#key   不可变,且唯一   int   str   tuple  float
#value  数据类型不限   整数   浮点数   字符串   布尔值  元组  列表  字典
#根据key:value 用逗号区分开来的
#  0=Ture  1=False
# 取值方式：无序数据
#根据key  取值    字典名[key]
d = {'name':'执着',
     'hobby':'学python',
     'age':18,
     'score':{'en':120,'math':99,'ch':'A'},
     'friend':['bay','xiaoxiao','向阳'],
     'good_man':True,
     1:'hello',
     0.02:'python',
     True:"这个value对应的key是布尔值",
     (1,2,3):'我就是元组大大'}
# print(d)
# print(len(d))
#找出名字最长的朋友
print(d['friend'][1])
print(d['friend'])
#取出执着同学的英语成绩  字典嵌套取值
# print(d['score']['en'])
#支持增删改
#增加  d[key]是不存在字典里面   就是新增
# d['salary']='20k'
# #如果key是不存在字典里面的  就是修改
# d['name'] = 'youyou'
#删除   根据key去删除
# d.pop('friend')  #指定删除
#随机删除
# d.popitem()
# print(d)
# #获取所有的key
# print(d.keys())
# #获取字典的所有value
# print(d.values())
