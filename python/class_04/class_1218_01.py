#异常处理：
#异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行
#一般情况下，在python无法正常处理程序时就会发生一个异常
#异常是python对象，表示一个错误
#当python脚本发生异常时我们需要捕获处理它，否则程序会终止执行
#异常：程序运行的过程中出现的问题或错误，都可以称之为异常

#每个异常包含的信息：出错的文件  行数  具体的代码  错误类型  错误信息

#异常处理：当程序运行出现异常的时候，对异常进行处理
#try....except...
#try:
    #监控的代码块
#except:
    #如果监控的代码块出现问题，怎么处理

# try:
#     file = open('test.txt', 'w', encoding='utf-8')
#     print('读操作之前')
#     result = file.read() #---异常出现在这里  程序要中断
#     print('读操作之后')
#     print('读操作获取的结果：{}'.format(result))
# except:
#     file.write('读操作报错了')
#     print('读操作报错了')
#
# print('python13期的同学们，晚上好!')

#try...except.... 错误类型 as e...
#每个异常包含的信息：出错的文件  行数  具体的代码  错误类型  错误信息
# print(a) #NameError: name 'a' is not defined
# 错误基类
#exception 常规错误的基类
#assertionError 断言语句失败
#attributeError 对象没有这个属性
#kyError  映射中没有这个键
#NameError 未声明/初始化对象（没有属性）
#SyntaxError  python语法错误
#IndenttationError  缩进错误
#BaseException 所有异常的基类
#BaseException 比 exception 抓的范围更广
#BaseException  exception  --万能的    缺点:逢错必抓，有内耗  优点:不会放过任何一个异常
#定位你的异常:明确的你错误类型  方便定位问题
# L = [1,2,3]
# try:
#     print('获取列表的数据', L[4])#---中断
#     file = open('test.txt', 'w', encoding='utf-8')
#     print('读操作之前')
#     # print('获取列表的数据', L[4])
#
#     result = file.read() #---异常出现在这里  程序要中断
#
#     print('读操作之后')
#     print('读操作获取的结果：{}'.format(result))
#
# except IOError as e:#抓取Exception 这种错误类型 取别名为e
#     file.write('读操作报错了:{}'.format(e))#把错误e写到file里面去
#     print('读操作报错了')
# except IndexError as e:
#     print('列表数据读取错误{}'.format(e))
#     file.write('读操作报错了:{}'.format(e))  # 把错误e写到file里面去
# print('python13期的同学们，晚上好!')

#常见的错误类型：NameError、invalid syntax
#注意代码的执行顺序 什么地方会中断  跑到except里面去
#一个异常里面可以写多个except
#一个异常里面不可以写多个try
#可以同时except多个异常？可以 except (IOError,InderError) as e
#try 里面可以嵌套try...except
# L = [1,2,3]
# try:
#     file = open('test.txt', 'w', encoding='utf-8')
#     try:
#         print('获取列表的数据', L[4])#---中断
#     except IndexError as e:
#         print('获取列表数据报错了:{}'.format(e))
#
#     print('读操作之前')
#     # print('获取列表的数据', L[4])
#     result = file.read() #---异常出现在这里  程序要中断
#
#     print('读操作之后')
#     print('读操作获取的结果：{}'.format(result))
#
# except IOError as e:#抓取Exception 这种错误类型 取别名为e
#     file.write('读操作报错了:{}'.format(e))#把错误e写到file里面去
#     print('读操作报错了')
# except IndexError as e:
#     file.write('读操作报错了:{}'.format(e))  # 把错误e写到file里面去
# print('python13期的同学们，晚上好!')


#try...except...finally
#try...except...else
#with...open...as ...上下文管理器

# L = [1,2,3]
# try:
#     file = open('test.txt', 'w', encoding='utf-8')
#     print('读操作之前\n')
#     # print('获取列表的数据', L[4])
#     result = file.read() #---异常出现在这里  程序要中断
#     TestReuslt = 'PASS'  #执行成功了
#     # file.write(TestReuslt)
#     print('读操作之后\n')
#     print('读操作获取的结果：{}'.format(result))
#
# except IOError as e:#抓取Exception 这种错误类型 取别名为e
#     TestReuslt = 'FAIL'
#     file.write('读操作报错了:{}'.format(e))#把错误e写到file里面去
#     print('读操作报错了\n')
#     # file.write(TestReuslt)
# finally:#用处：不管你是运行到try  except finally最终都会运行
#     #不管是try  还是except  我都要用的时候
#     file.write('我执行完毕了，我是finally')  # 把错
#     file.write(TestReuslt)
# print('python13期的同学们，晚上好!')

#try...except...else
#try 和 else是一起使用的   try不出错else就会执行  try出错，else就不执行
#else和finally 的区别是  finally是不管try下面的监控代码正确与否，finally都会执行
#else 是和try一起使用，try下面的代码错误，else就不会执行
# L = [1,2,3]
# try:
#     file = open('test.txt', 'w', encoding='utf-8')
#     print('读操作之前')
#     # print('获取列表的数据', L[4])
#     result = file.read() #---异常出现在这里  程序要中断
#     TestReuslt = 'PASS'  #执行成功了
#     # file.write(TestReuslt)
#     print('读操作之后')
#     print('读操作获取的结果：{}'.format(result))
#
# except IOError as e:#抓取Exception 这种错误类型 取别名为e
#     TestReuslt = 'FAIL'
#     file.write('读操作报错了:{}'.format(e))#把错误e写到file里面去
#     print('读操作报错了')
#     # file.write(TestReuslt)
# else:#用处：不管你是运行到try  except finally最终都会运行
#     #不管是try  还是except  我都要用的时候
#     file.write('我执行完毕了，我是finally')  # 把错
#     file.write(TestReuslt)
# print('python13期的同学们，晚上好!')

#with...as ...上下文管理器
# file = open('test.txt','w+',encoding='utf-8')
# file.write('妻子的浪漫旅行')

#文件是否关闭
# print('1:',file.closed)
# file.close()
# print('2',file.closed)

# with open('test.txt','w+',encoding='utf-8') as file:
#     file.write('妻子的浪漫旅行')
# print('2',file.closed)