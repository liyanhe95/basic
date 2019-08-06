#file txt 日志  不包括mp4 excel html
#处理：读、写  (与光标有关系)
#什么时候用：想用就用
#存储数据的操作

#读处理
#第一步：打开文件  open() file
# file = open('python13.txt',encoding='UTF-8') #我打开的文件存在file文件里面
# print(file.read())#默认是读取文件中的所有内容(把内容一次性读取出来)，保持格式
# print('*************')
# print(file.read(5)) #读取指定长度的内容
# print('*************')
# print(file.readline())  #按行读取,每次只能读取一行的内容
# print(file.readlines())#按行读取，读取所有行内容--返回列表 每一行是列表的一个元素
#读出前10行诗句
# for i in range(10):
#     print(file.readline())
# count = 0
# while count<10:
#     print(file.readline())
#     count+=1
#读出5-8行的数据
# for i in range(10):
#     if 5<=i<=8:
#         print(file.readline())
#     else:
#         file.readline()
#有中文的时候注意设置编码为utf-8

#写处理
# open()函数
#文件打开的模式
# r r+  只读        读写
# file = open('python13.txt','r+',encoding='utf-8') #我打开的文件存在file文件里面
# file.write('li')
#先读在写  写在最后面
#先写  覆盖写
# w w+  只写        只写的读取文件会报：not readable
# file = open('python13.txt','w',encoding='utf-8')#清空文件
# file.readline()
# file.write('那年夏天')
#如果先写在读的话  打开文件是空文件，两个方法可以解决次问题
#1 先写再重新打开文件，再读
#2 file.seek(0,0),再读 #重新改变光标的位置   移动的量  相对位置   0-开头  1--当前位置(此处不支持，当你是二进制文件的时候才支持) 2--尾巴
#  file.seek(3,0)  只能写3的倍数
#ASCII 编码  一个英文一个字节
#GBK编码   支持中文
#UTF-8 编码   一个字符占3个字节
#ascii-->decode-->UTF-8-->encode gbk
# file = open('yu.txt','w') #如果文件不存在的话 可以新建一个文件，如果文件存在的话，先清空再做其他操作
# file.close()#关闭文件
# a a+  只能追加写  追加读写(注意光标的位置)
file = open('python13.txt','a+',encoding='utf-8')#如果文件存在的话，针对文件操作，如果文件不存在的话，会新建一个文件再进行操作
file.write('you name')
file.seek(0,0)
print(file.read())
file.close()
#只读模式下 去进行写操作 io.UnsupportedOperation: not writable
#什么时候会使用？？？
#写日志  生成html报告的时候会用到

