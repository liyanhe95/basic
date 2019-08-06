#继承  类的拓展和重写  extend override
#电商平台：平台名称 特征（feature） 销售模式 创始人
#登录 物流 支付方式  打折活动 计算收银的功能 未付款提醒

#实际
#平台名称  特征（买什么比较多） 创始人
#功能：登录 支付方式 计算收银的功能
#思路 公共的
#电商平台：
# 平台名称 特征 feature 销售模式 创始人
# 登录功能 物流 支付方式 打折活动 计算收银的功能 未付款提醒 评价 客服 会员

#父类：
#平台名称 特征（卖什么比较多）创始人
#功能：登录 支付方式 计算收银的功能
#登录功能：
#1. 用户名统一规定为 huahua 密码统一规定为 123456
#2.如果输入用户名和密码正确 就提示登录成功，返回True(布尔值类型）
#3.如果用户名和密码不匹配或者不正确，那么就显示登录失败，用户名或密码不正确，返回False(布尔值类型）
#支付方式：有3种 一种是微信支付 一种是支付宝支付 一种是银联支付
#一个优惠的功能：随机发送不同额度金额的优惠金额（金额范围在10-50之间）
#写2个子类：京东类 和 淘宝类
import random
class BaseShop:
    #这是电商平台的公用父类
    def __init__(self,name,feature,boss,mode):
        self.name = name #平台名称
        self.feature = feature  #特征
        self.boss = boss #创始人
        self.mode = mode #模式

    def login(self):
        name = input('请输入用户名')
        password = input('请输入密码')
        #设置初始值 name=huahua password=123456
        if name == 'huahua' and password == '123456':
            print('登录成功！')
            result = True
        else:
            print('登录失败，用户名或密码不正确')
            result = False

        return result #返回登录的结果

    def alipay(self):#支付宝
        print('支持支付宝支付')

    def wechatpay(self):#微信
        print('支持微信支付')

    def unionpay(self): #银联支付
        print('具备银联支付功能')

    def discount_money(self):#优惠的金额
        money = random.randint(10,50)
        print('此次享有的优惠金额是{}'.format(money))
        return money





