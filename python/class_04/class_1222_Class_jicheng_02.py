#类的继承 apple 通过手机量身高以及物体之间的距离 测距仪

from basic.python.class_04.class_1222_init_function_01 import Phone

class ApplePhone(Phone):#继承Phone类
    #这是一个苹果手机类，标记苹果手机的功能和属性
    def measure(self):#测距仪  --拓展  extend  在继承的情况下，子类有父类不具有的函数
        print('可以帮我们测量身高或者是距离')
    def music(self,song):  #重写 子类重写了父类的同名方法 override
        print('可以播放{}'.format(song))
#ApplePhone继承了Phone类
#ApplePhone 是子类
#Phone      是父类
#ApplePhone继承了Phone所有的方法和属性---->说明了什么问题？
#继承可以用它的方法和属性，但是不可以改变它
ApplePhone.send_message('前方高能，各位请注意，华华老师来了')
#父类里面有初始化函数，子类创建对象的时候，要传参？---一定要传参，除非有默认值，那可以传也可以不传
ApplePhone('iphone8',8000,'ios','gold',6.5).call()
#调用ApplePhone的专有函数
ApplePhone('iphone8',8000,'ios','gold',6.5).measure()
#问题是：父类Phone 可以调用子类ApplePhone的measure方法？--绝对不可以
#如果发生继承，爸爸的是我的，我的还是我的

#使用场景  --- 想用就用
#有多个类  子类和父类的方法大部分重叠时
class OppoPhone(Phone):
    def best_function(self):
        print('充电5分钟通话两小时')

