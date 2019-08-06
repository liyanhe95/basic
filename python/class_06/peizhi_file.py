import configparser #ConfigParser配置类  专门来读取配置文件的
#配置文件：结尾以 .ini、.conf、 .config 、.properties、xml

#配置文件一般是什么样的

#section 片段/区域 [区域名]
#option 相当于字典里面的key，一个个配置的选项
#value  相当于字典里面的value

#怎么用呢?
# cf = configparser.ConfigParser()
# cf.read('case.conf',encoding='utf-8')#open
# # value = eval(cf.get('TeacherInfo','t_name'))#读值方法1
# # value = cf.getfloat('TeacherInfo','grade')
# # value = cf.getint('TeacherInfo','avg_age')
# value = cf.getboolean('TeacherInfo','age')
# # value = cf['StudentInfo']['class_name']  #读值方法2
# print(value)
# print('值的类型',type(value))
#注意的点：读取出来的值都是字符串 对值去进行处理 可以用eval函数
class ReadConfig:
    #读取配置文件的类
    def __init__(self,file):
        self.cf = configparser.ConfigParser() #为什么要赋值给self.cf  方便后面的方法调用
        self.cf.read(file,encoding='utf-8')

    def get_value(self,section,option):
        return self.cf.get(section,option)

    def get_int(self,section,option):
        return self.cf.getint(section,option)

    def get_float(self,section,opction):
        return self.cf.getfloat(section,opction)

    def get_boolean(self,section,opction):
        return self.cf.getboolean(section,opction)



if __name__ == '__main__':
   res = ReadConfig('case.conf').get_boolean('TeacherInfo','age')
   print(res)