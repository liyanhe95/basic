# 日志   日志是什么  为什么要学习日志
# 在哪一行  那个文件  错误级别  错误发生时间
# 记录软件/应用程序/代码的运行日志
# 方便我们后期去定位复查问题

# 学好了之后怎么用
# 先学完了之后再来问

# 日志里级别有哪几种
# debug info warning error critical
# 从左往右越来越严重
# root logger  收集日志的容器 如果你不定义一个logger，那么就默认使用root logger
# 收集warning以上级别的信息
# handlers 渠道  控制台 console(默认渠道)  文本 file_handler
# pre-defined format 按照提前设置好的格式进行输出--> 级别：日志收集器的名字：日志信息
# python 有一个自带的日志系统  logging
import logging
class MyLog:
    def my_log(self, level, msg):
        # 写一个属于自己的日志系统
        # 收集器--创建一个日志收集器 getLogger()函数
        my_logger = logging.getLogger('python13')  # 创建一个日志收集器
        my_logger.setLevel('DEBUG')  # 设置日志级别,给这个日志收集器setLevel

        # 格式：规定日志输出的格式
        formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-[%(filename)s]-[%(name)s]-[日志信息]:%(message)s')

        ch = logging.StreamHandler()  # 创建一个输出到控制台渠道
        ch.setLevel('DEBUG')  # 给渠道设置级别
        ch.setFormatter(formatter)  # 设置日志输出格式

        # 输出到指定的文件
        fh = logging.FileHandler('python13.log', encoding='utf-8')
        fh.setLevel('INFO')
        fh.setFormatter(formatter)  # 设置日志输出格式

        # 对接 日志收集器与输出渠道进行对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        #去掉日志的重复 每次收集完毕之后  记得移除掉日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):#输出debug级别的信息
        self.my_log('DEBUG',msg)

    def info(self,msg):#输出info级别的信息
        self.my_log('INFO',msg)

    def warning(self,msg):#输出warning级别的信息
        self.my_log('WARNING',msg)

    def error(self,msg):#输出error级别的信息
        self.my_log('error',msg)

    def critical(self,msg):
        self.my_log('critical',msg)#输出critical级别的信息


if __name__ == '__main__':
    my_logger = MyLog()
    my_logger.debug('我是debug')
