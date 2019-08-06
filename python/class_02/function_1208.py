#函数的定义:实现某个指定的功能 重复使用
# type()
# len()
# range()
#函数有啥作用:可以提高代码的复用性
#函数的具体语法：关键字  def
#def 函数名(参数1,参数2,参数3):
    #函数体:本函数要实现的功能
    #return 表达式
#def 顶格写 表示这是一个函数
#函数名  小写  不同的字母与数字之间用下划线隔开  不能以数字开头
#参数的个数可以大于等于0
#函数体是函数的子代码  要有缩进  写自己想实现的功能即可
#return后面的表达式 >=0 个
#return 就是当你调用函数的时候 会返回return后面的表达式的值
#如果return后面没有表达式  写没写  没有区别
#如何调用函数   函数名(对应参数个数)
def radio_machine():
    print('就是一个复读机，只会说：你好！！！')
    return  #隐式的添加一个return
res = radio_machine()  #res 存储返回的值
print('函数的返回值是：{}'.format(res))
#函数里面return的表达式个数
#==1 返回你指定的数据类型
#>1 返回的是元组类型
#==0 返回None
def add():
    result = 8 + 8
    print(result)
    return result
res1 = add()+ 20
print(res1)


#请你拿到add()运行的求和结果  再去加20   输出到控制台

