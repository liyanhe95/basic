#类划分的标准是什么：具有相同特征或者的行为的一类事物
#对象   类里面的一个具体实例

#编写手机类  特征/功能
#品牌名 价格 操作系统 颜色 尺寸
#打电话 发短信 看视频 玩游戏 拍照 听音乐 阅读 导航 闹钟
#对象 oppo 4500 Android 黑色 5.5
#打电话 发短信 看视频 拍照 听音乐 导航 闹钟

#python 的语法
#类语法
#class ClassName:
    #'类的帮助信息' 类文档字符串
    #class_suite 类体

#1 类体里面可以包含：类属性和类函数
#2 类名：见名知意 首字母大写其他首字母大写 驼峰命名
#3 创建一个对象/实例化
#创造实例：a=类名() #那么a就是一个对象
class Phone:
    '这个类是手机类，专门标记手机的属性和功能'
    brand_name = 'oppo'#类属性/类变量
    price = 4500
    colour = 'black'
    os = 'Android'
    size = 5.5

    #功能 类的函数(类的方法)  方法 == 函数
    def call(self): #可以打电话   一般是用self   叫对象方法(因为只能通过对象来调用)
        # print('self的值:',self)  #写self就是需要把类本身传进来，用一个参数来接收对象本身
        print('可以打电话')
        return 666

    @staticmethod #静态方法
    def send_message(content):#可以发送短信
        #静态方法里面调用对象方法
        Phone().music()  #最好的方法是创建一个对象来调用对象方法
        print('发送短信：{}'.format(content))

    @classmethod
    def watch_vedio(cls,**kwargs):#看视频
        #类方法里面调用对象方法和静态方法
        cls.send_message('hello')
        cls().call()
        Phone().music()
        print('可以看视频{}'.format(kwargs))

    def take_shot(self):#拍照
        self.send_message('hello')  #类的方法(对象方法)里面调用静态方法方法
        self.watch_vedio(song='lili')#类的方法(对象方法)里面调用类方法
        self.call()

        Phone.send_message('老师你好')
        Phone.watch_vedio(song='陈')
        Phone().call()

        print('可以拍照')

    def music(self):#听歌
        print('可以听歌')

    def phone_info(self):#描述手机
        print('手机的品牌是{}，价格是{}，颜色是{}，操作系统是{}'.format(self.brand_name,Phone.price,self.colour,Phone.os,self.size))
#对象-->创建对象:类名()
phone = Phone()  #对象
#通过对象访问它的属性 对象.属性名
#结论：类和对象可以直接访问属性，并且获得他们的值
# print('品牌名:',phone.brand_name)
# print('价格:',phone.brand_name)
# print('尺寸:',phone.size)
# print('品牌名:',Phone.brand_name)

#类里面的方法名:对象.方法名()
#self 是什么东西  self指的是对象本身
#调用类方法的时候必须得是对象来调用
# print('phone的值',phone)
# phone.call()
#对象方法只能通过对象访问
#静态方法 @staicmethod 放在函数上面 来标记/装饰
#静态方法可以通过类和对象来调用
# Phone.send_message()
# phone.send_message()
#类方法 @classmethod 放在函数上面 来标记/装饰
#静态方法可以通过类和对象来调用
# Phone.watch_vedio()
# phone.watch_vedio()
# phone.music()
# phone.take_shot()
# phone.send_message()
# phone.watch_vedio()

#应用场景
#类的方法和普通函数有啥区别？
#1 除了对象方法必须有self 类方法必须有cls参数以外，其他的并无区别
#参数类型:位置参数 默认参数 关键字参数 动态参数都有
#return 都支持
#2 必须通过该类的对象或是该类来访问 不能直接访问
# phone.send_message('你好')
# phone.watch_vedio(vedio1='将夜',vedio2='火王')
# phone.call()

# phone.phone_info()
# phone.take_shot()
# phone.send_message('hello')
# phone.watch_vedio(vedio1='将夜',vedio2='火王')

#1 类方法  静态方法  对象方法都可以通过对象去访问
#2 类方法  静态方法可以通过类去访问
#3 对象方法为什么叫对象方法因为它只能通过对象去访问
#4 类的属性通过类和对象去调用 不能直接在类外面去调用这个值，也不能在函数里面直接调用这个值
#5 类的方法和普通函数有啥区别？
#a 除了对象方法必须有self 类方法必须有cls 参数以外 其他并无区别
#b 都支持return 位置参数 默认参数 关键字参数 动态参数
#对象方法要访问类方法和静态方法可以通过self.方法名来完成调用
#如果在静态方法里面去调用其它方法，你始终要记住，静态方法没有传对象，
#也没有传类进来的，这个时候只能通过类去访问它的类方法，只能通过对象去访问对象方法

#如果在类方法里面去访问对象方法以及静态方法或者是类方法，可以通过类去访问，
#也可以通过对象去访问cls()以及Phone()它是同一个意思

#注意：不管什么时候静态方法和类方法和对象方法都可以通过对象访问
#但是只有静态方法和对象方法支持类直接访问
#属性可以通过对象和类同时访问

