#京东类 用户购买了东西 只能选择微信支付 银联支付 不支持支付宝支付

# 一个结算的功能：结算的时候根据用户选择 结算的时候根据用户输入用户信息以及金额以及支付方式作出如下的反馈
#先判断用户是否登录成功 登录成功后提示用户名 然后用户输入金额
#1）微信支付 就可以享受优惠
#2）选择银联支付就不享受优惠
#3）选择支付宝提示不能支付，请重新选择支付
from basic.python.class_05.class_extend_override_1224_01 import BaseShop
class Jd(BaseShop):#继承Baseshop

    def count(self):#结算
        #首先用户登录
        if self.login(): #因为登录后，返回的是布尔值
            print('开始结算')
            money = input('请输入你的结算金额')
            if money.isdigit():
                money = int(money)
            else:
                print('输入有误，请重新输入')

            while True:
                pay_way= input('请选择结算方式  alipay:支付宝，wechat:微信，unionpay:银联')
                if pay_way == 'wechat':
                    self.wechatpay()
                    discount_money = self.discount_money()
                    if money >= discount_money:
                        count_money = money-discount_money
                        print('你选择的是微信支付，可以享受优惠，折后价是{}'.format(count_money))
                        return count_money

                    else:
                        print('总价大于优惠金额，不支持优惠')
                        return money

                elif pay_way == 'unionpay':
                    self.unionpay()
                    print('你选择的是银联支付，不可以享受优惠')
                    return money
                    break

                elif pay_way == 'alipay':
                    print('不支持此支付方式，请重新选择支付')
                    continue

                else:
                    print('支付方式选择有误，请重新选择')
                    continue





# jd = Jd('京东','电子产品','刘强东','自营')
# # print(jd.feature)
# # print(jd.wechatpay())
# jd.count('90')