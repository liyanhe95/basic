# 初始化函数

class Phone:
    '这个类是手机类，专门标记手机的属性和功能'

    # 初始化函数__init__()，作用：属性参数化
    def __init__(self, brand_name, price, colour, os, size):  # 对象方法  别的地方用属性名
        self.brand_name = brand_name  #对象属性，只能通过对象调用
        self.price = price   #赋值给对象属性，只能通过对象访问，方便后期调用
        # Phone.price=price  #把price赋值给Phone类，只能通过类去访问，对象是属于类的，对象拥有类里面属性和方法的所有属性权
        self.colour = colour
        self.os = os
        self.size = size

    # 功能 类的函数(类的方法)  方法 == 函数
    def call(self,name='lili'):  # 可以打电话   一般是用self   叫对象方法(因为只能通过对象来调用)
        print('self的值:', self)
        print('可以给{}打电话'.format(name))

    @staticmethod  # 静态方法
    def send_message(content):  # 可以发送短信
        # 静态方法里面调用对象方法
        print('发送短信：{}'.format(content))

    @classmethod
    def watch_vedio(cls):  # 看视频
        print('可以看视频')

    def take_shot(self):  # 拍照
        print('可以拍照')

    def music(self):  # 听歌
        print('可以听歌')

    def phone_info(self):  # 描述手机
        print('手机的品牌是{}，价格是{}，颜色是{}，操作系统是{},尺寸是{}'.format(self.brand_name, self.price, self.colour, self.os, self.size))

if __name__ == '__main__':

# 对象-->创建对象:类名()  对象拥有类里面所有属性和方法的访问权
#如果你用了初始化函数，那么你在创建对象的时候必须要传参
    phone = Phone('华为',2500,'pink','Android',5.0)
    phone.call()
    phone.phone_info()

#如果说静态方法和类方法里面与类的属性没有半毛钱关系，我就可以定义成静态方法或类方法，方便我调用的时候，不需要传那么多参数。
#因为可以直接通过类去调用（前提是不需要调用类属性）

#静态方法和类方法之间有什么区别？



