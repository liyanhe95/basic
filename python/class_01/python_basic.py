#-*- coding:utf-8
#@time:2019\4\14
#@author:李艳荷
#@Email:976621712
#@File:
#@Software:PyCharm
"""
1、安装python
2、安装pycharm
设置pycharm的字体大小和颜色
file--setting--editor--color scheme font
3、python的第三方库非常丰富
4、第三方库都是需要安装才可用使用
5、安装的方式
a、pycharm 在线安装 file--setting--project interpreter（项目解释器）
b、在线安装  cmd -->pip install requests（库名）
   翻墙 VPN
   国内源：pip install requests -i ip地址
c、离线安装
XXX.tar.gz rar zip
解压
把解压后的文件copy到python的安装路径下去
e:回车 进入到相关盘
cd 进入到文件夹
python setup.py install


file   文本文件
directory   文件夹（放静态资源：css、js、html等）
python package  python的包（整理python代码）
python file
html file
标识符（取名字），你来命名的都叫标识符
项目名 包名 文件名 函数名 变量名  类名
标识符的规范
1.数字  字母  下划线 组成 （不能包含中文及特殊符号其他的）
2.不能以数字和特殊字符开头，
3.字母和数字之间可用下划线隔开，方便阅读
4.见名知意
5.不能以关键字命名
import keyword
print(keyword.kwlist)
eg：class_1129_basic
注释
单行注释 #
#多行注释：成对的 '''
快捷方式  ctrl+/ 同时按住

"""
#缩进   python中用缩进区分代码之间的层次
# a = 10
# if a == 1:
#     print('a的值为1')
# else:
#     print('a的值不为1')
print('hello world')  #函数 输入内容到控制台
b = input('请输入一个数据\n')#函数 从控制台获取数据  input中获取的数据全部都是字符串类型
print(b)

"""
\ 续行符
\n 换行符
\0 空
\t 水平制表符，用于横向跳到下一制表符
在字符串定界符前的前面加上字母r，那么该字母字符串将原样输出，其中转义将不转义
模块名尽量使用小写字母，类名采用单词首字母大写
"""