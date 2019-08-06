# 高级题：
#写一个警察类： 2个对象
#警察具有这些属性： 代号 真实姓名 年龄 类别:police
#技能：开枪，但是开枪前先要知道 是否是坏蛋，不能对平民开枪、 指认、 抓坏蛋 、run 跑起来很快

#写一个坏人类：3个对象
#坏人具有这些属性：绰号 真实姓名 年龄 类别:badegg
#技能：开枪，可以对警察和平民开枪 、 run 跑起来很快 、偷东西、抢银行

# 写一个平民类： 5个平民对象  牺牲了对象就不见了  如果存在列表里面就需要pop
# #平民具有这些属性：昵称 真实姓名 年龄 类别:people

#规则：一共有5个平民 3个坏蛋 2个警察，所有的都只能指认一次，按顺序来。同类人之间不能相互指认
#1：坏蛋：pitt 河畔 海绵---->一起 意见统一才能出击(少数服从多数)，如果指认比例平局就作废没人牺牲，如果去抢银行偷东西，那么就不参与指认。
#2：平民：花花 七月 晴天 简爱 阿牛---->一起 意见统一(少数服从多数)才能出击，不管是指认了警察还是坏蛋都会牺牲，如果指认比例平局就作废没人牺牲，
#3：警察： 挖矿 月亮---->一起 意见统一才能出击，才能出击，不统一作废。如果正确的指认了坏蛋，开枪，坏蛋牺牲，如果指认了平民，指认无效，这一轮结束

#最后结果：（需要用for循环或者while循环，要随机指认的需要用到随机函数）
#如果坏蛋为0 那么警察、平民赢
#如果平民为0 警察、平民输
#如果警察为0 警察、平民输

class Police:
    #这是一个警察类
    def __init__(self,code,real_name,age):
        self.code = code
        self.real_name = real_name
        self.age = age

    def shoot(self):#警察开枪
        print('警察开枪了')

    def point_out(self):#指认技能
        print('指认')

    def grasp_badegg(self):#抓坏蛋
        print('抓坏蛋')

    def run(self):#跑起来很快
        print('跑起来很快')

    def police_one(self):
        print('代号是{}，真实性名是{}，年龄是{}'.format(self.code,self.real_name,self.age))

    def police_two(self):
        print('代号是{}，真实性名是{}，年龄是{}'.format(self.code,self.real_name,self.age))

class BadEgg(Police):
   #这是一个坏蛋类
    def badegg(self):#坏蛋开枪
        print('坏蛋开枪了')

    def steal(self):#坏蛋偷东西
        print('偷东西')

    def rob(self):#坏蛋抢银行
        print('抢银行')

    def badegg_one(self):
        print('绰号是{}，真实姓名是{}，年龄是{}'.format(BadEgg.code,BadEgg.real_name,BadEgg.age))

    def badegg_two(self):
        print('绰号是{}，真实姓名是{}，年龄是{}'.format(BadEgg.code, BadEgg.real_name, BadEgg.age))

    def badegg_three(self):
        print('绰号是{}，真实姓名是{}，年龄是{}'.format(BadEgg.code, BadEgg.real_name, BadEgg.age))

#技能：run 跑起来很快 、指认技能
class People(Police):
    def people_one(self):
        print('昵称是{}，真实姓名是{}，年龄是{} '.format(People.code,People.real_name,People.age))

    def people_two(self):
        print('昵称是{}，真实姓名是{}，年龄是{} '.format(People.code,People.real_name,People.age))

    def people_three(self):
        print('昵称是{}，真实姓名是{}，年龄是{} '.format(People.code,People.real_name,People.age))

    def people_four(self):
        print('昵称是{}，真实姓名是{}，年龄是{} '.format(People.code, People.real_name, People.age))

    def people_five(self):
        print('昵称是{}，真实姓名是{}，年龄是{} '.format(People.code,People.real_name,People.age))