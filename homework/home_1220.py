#1：编写手机类 机器人类 要求至少有5个属性，5个方法（要包含对象方法 类方法 静态方法）
#编写机器人类
#特征：品牌、价格、颜色、材质、尺寸
#功能：聊天、学前教育、扫地、端水、做饭、智能跟随
class Robot:
    '这是一个智能机器人类，有机器人的属性和功能'
    brand_name = '小艾'#类的属性
    price = 599
    colour = 'pink'
    material = 'plastic'
    size = '46*28*30'

    def chat(self,name='huahua'):#对象方法
        print('可以和{}聊天'.format(name))

    @staticmethod
    def music():
        Robot().chat('lili')
        print('可以听音乐')

    @classmethod
    def clear(cls): #在类方法中访问静态方法、对象方法
        cls.music()  #cls是类本身
        Robot.music()
        cls().music()   #cls是类本身，故cls和Robot是一样的，都是创建一个对象
        cls().chat('mother')
        print('可以帮我扫地的')

    def education(self):
        self.music() #对象方法  在对象方法中访问静态方法、类方法、对象方法
        Robot.clear()
        Robot.music()

    def follow(self):
        print('可以时刻跟随主人')


robot = Robot()
#访问类属性：类和对象可以直接访问，并获得他们的值
print('颜色是：',Robot.colour) #类名.属性名
print('大小是：',robot.size)#对象名.属性名

#访问类的方法
robot.chat()#利用对象访问对象方法

robot.music()#利用对象访问静态方法
Robot.music()#利用类访问静态方法

robot.clear()#利用对象访问类方法
Robot.clear()#利用类访问类方法

robot.education()#利用对象访问对象方法



