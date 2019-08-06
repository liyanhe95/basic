#日志   日志是什么  为什么要学习日志
#在哪一行  那个文件  错误级别  错误发生时间
#记录软件/应用程序/代码的运行日志
#方便我们后期去定位复查问题

#学好了之后怎么用
#先学完了之后再来问

#日志里级别有哪几种
#debug info warning error critical
#从左往右越来越严重
#root logger  收集日志的容器 如果你不定义一个logger，那么就默认使用root logger
#收集warning以上级别的信息
#handlers 渠道  控制台 console(默认渠道)  文本 file_handler
# pre-defined format 按照提前设置好的格式进行输出--> 级别：日志收集器的名字：日志信息
#python 有一个自带的日志系统  logging
import logging
#写一个属于自己的日志系统
#收集器--创建一个日志收集器 getLogger()函数
my_logger = logging.getLogger('python13')#创建一个日志收集器
my_logger.setLevel('DEBUG') #设置日志级别,给这个日志收集器setLevel

#格式：规定日志输出的格式
formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-[%(filename)s]-[%(name)s]-[日志信息]:%(message)s')
#%(asctime)s   收集当前系统时间
#%(levelname)s 日志级别
#%(filename)   日志模块名
#%(name)s      日志收集器名字
#%(leveno)s 数字形式的日志级别
#%(levenames)s 文本形式的日志级别
#%(filename)s  调用日志输出函数的模块的文件名
# %(pathname)s  调用日志输出函数的模块完整结合，可能没有
# %(module)s 调用日志输出函数的函数名
#%(lineno)d  调用日志输出函数所在的代码行
#输出渠道--指定输出渠道
ch = logging.StreamHandler()#创建一个输出到控制台渠道
ch.setLevel('ERROR')#给渠道设置级别
ch.setFormatter(formatter) #设置日志输出格式

#输出到指定的文件
fh = logging.FileHandler('python13.log',encoding='utf-8')
fh.setLevel('INFO')
fh.setFormatter(formatter)#设置日志输出格式

#对接 日志收集器与输出渠道进行对接
my_logger.addHandler(ch)
my_logger.addHandler(fh)

my_logger.debug('这是一个debug信息')
my_logger.info('这是一个info信息')
my_logger.warning('这是一个warning信息')
my_logger.error('这是一个error信息')
my_logger.critical('这是一个critical信息')




