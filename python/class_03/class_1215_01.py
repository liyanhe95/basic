#模块的导入
#导入到当前的模块中来

#import
#from...import...   #可以具体到函数名及类名，但是至少到模块名（推荐使用）
#from...import...as
#from...import *
#除了顶级目录，导入你要引用的文件， 需要一层一层剖开
# import basic.python.class_03.class_1213_01
# import basic.python.class_03.class_1213_01 as python
#当你导入的文件路径超长的时候，当你导入的模块名很长的时候（可以取别名）
# from basic.python.class_03.class_1213_01 import eat
#调用eat函数
# basic.python.class_03.class_1213_01.eat('胡萝卜','玉米','螺蛳粉')
# python.eat('胡萝卜','玉米','螺蛳粉')
# eat('胡萝卜','玉米','螺蛳粉')
# from basic.python.class_03.class_1213_01 import *
# eat('优乐美')
# student_info('python13','li',20)

#os 学习
#python里面的os模块有许多方法让我们通过代码实现创建，删除和更改目录，具体如下
#os.getcwd():显示当前的工作路径，只是具体到路径，不具体到文件
#os.path.realpath(path):返回path的真实路径 如果参数是:_file_就说明是文件所在的绝对路径
#os.path.join(a,b):连接两个部分的路径，组成一个完整的路径
#os.mkdir(路径名字):在某个目录下创建一个新目录
#os.rmdir(路径名字):删掉一个目录
#os.listdir():获取当前路径下的目录列表，返回列表格式数据
#os.path.isdir:判断当前文件是否是目录，返回布尔值
#os.path.isfile:判断当前文件是否是文件，返回布尔值


#绝对路径  相对路径
# f1 = open('python.txt',encoding='utf-8')  #相对路径
# print(f1.read())
#
# f2 = open(r'I:\pyc\basic\python\class_03\python.txt',encoding='utf-8') #绝对路径
# print(f2.read())
import os
#可以获取到绝对路径  __file__表示当前模块文件  具体到文件名(模块名)
# real_path = os.path.realpath(__file__)
# print('绝对路径',real_path)
#
# pwd_path = os.getcwd()  #具体到当前工作目录
# print('当前工作目录',pwd_path)
#
# file_list = os.listdir(pwd_path)  #返回值是列表
# print('当前目录下的所有文件名',file_list)
#
# for file in file_list:
#     if os.path.isdir(file):#判断是否是文件夹，返回的是布尔值
#         print('{}是一个文件夹'.format(file))
#     elif os.path.isfile(file): #判断是否是文件，返回的是布尔值
#         print('{}是一个文件'.format(file))
#
#新建  删除   mkdir  rmdir
# os.mkdir('whereas') #新建在当前目录下
# #make directory
# os.rmdir('whereas')
# #remove directory

#多级新建  不能跨级创建文件 必须一级一级新建
#如果跨级新建的时候  要注意前面的路径已经存在 否则就会报错
# os.mkdir('whereas/AI')
#删除的时候要注意是否没有子目录  为空  只能一级一级的删除，不可以多级删除
#非空目录是否支持强制删除
# os.rmdir('whereas/AI')


pwd_path = os.getcwd()  #具体到当前工作目录
print('当前工作目录',pwd_path)

# print(os.path.join(pwd_path,'那年夏天')) # 拼接路径  绝对路径 os.path.join(prefix,suffix)
# os.mkdir(os.path.join(pwd_path,'那年夏天'))

print(pwd_path+'\youyou')
os.mkdir(pwd_path+'\youyou')