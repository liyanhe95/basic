# 1：如下2题，请分开2个作业提交
# 基础题：
# 人和机器猜拳游戏写成一个类，有如下几个函数：
# 1）函数1：选择角色 1曹操 2张飞 3刘备
# 2）函数2：角色猜拳 1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
# role_win = 0
# computer_win = 0
# draw_win = 0
# import random
# class Person_Vs_Machine:
#     def __init__(self):
#         pass
#
#     def choose_role(self):
#         dict_role = {'1':'曹操','2':'张飞','3':'刘备'}
#         while 1==1:
#             role_choice = input('选择角色   1：指定   2：随机')
#             if role_choice == '1':
#                 while 1==1:
#                     role_number = input('请输入你的角色编号 1:曹操  2:张飞  3:刘备')
#                     if role_number in dict_role.keys():
#                         print('你选择的角色是{}'.format(dict_role[role_number]))
#                         break
#                     else:
#                         print('选择有误，请重新输入')
#                         continue
#                 break
#             elif role_choice == '2':
#                 role_number = random.randint(1,3)
#                 print('随机生成的角色是{}'.format(dict_role[str(role_number)]))
#                 break
#             else:
#                 print('选择的项不存在请重新输入')
#                 continue  # 终止本次循环，继续下次循环
#         return dict_role[str(role_number)]

import random #导入生成随机数模块
class Human_VS_Pc:
    #定义一个人机大战类
    def __init__(self):   #初始化方法
        self.fist_dict={'1':'剪刀','2':'石头','3':'布'}
    def choose_role(self):  #选择角色
        role_dict={'1':'曹操','2':'张飞','3':'刘备'}
        #选择方案：随机  用户自己选择（拓展while）
        while True:
            choice=input('是选择角色还是随机分配角色   1：指定   2：随机')
            if choice=='1':  #指定
                while  True:
                    role_num=input('请输入你的角色编号： 1：曹操 2：张飞  3：刘备')
                    if role_num in role_dict.keys():    #获取字典所有key的值
                        print('你选择的角色是{}'.format(role_dict[role_num]))
                        break   #退出里层循环
                    else:
                        print('输入错误，请重新输入')
                        continue
                break   #退出外层循环
            elif choice=='2':  #随机指定
                role_num=random.randint(1,3)#利用randint随机生成一个整数 1-3之间
                print('随机生成的角色是{}'.format(role_dict[str(role_num)]))
                break   #终止循环
            else:
                print('选择的项不存在请重新输入')
                continue  #终止本次循环，继续下次循环
        return role_dict[str(role_num)]   #坑  类型的坑
    def role_fist(self):  #角色出拳  #可以把 role_name作为一个位置参数
        #1剪刀 2石头 3布
        role_name=self.choose_role()  #先选角色
        while True:
            fist_num = input('角色出拳：1:剪刀 2:石头 3:布')
            if fist_num in self.fist_dict.keys():  #获取字典的所有key   成员函数
                print('{},选择的拳是{}'.format(role_name,self.fist_dict[fist_num]))
                break
            else:
                print('{}出拳的数字不对，请重新输入'.format(role_name))
                continue
        return int(fist_num)
    def pc_fist(self):  #电脑出拳
    # 1剪刀 2石头 3布
        fist_num=random.randint(1,3) #从1-3里面随机选择一个数字
        print('电脑随机出的是{}'.format(self.fist_dict[str(fist_num)]))
        return fist_num
    def role_vs_pc(self):  #双方对战
        role_win=0   #角色赢了
        pc_win=0 #电脑赢了
        ping=0
        # role_name = self.choose_role()
        while True:
            role=self.role_fist()#角色出拳  #这里可以把role_name 作为参数传进来，然后角色每次都是一个角色
            pc=self.pc_fist() #电脑出拳
            if (role-pc) in [2,-1]:
                print('恭喜你赢了')
                role_win+=1#赋值运算
            elif (role-pc)==0:
                print('双方平局')
                ping+=1
            else:
                print('电脑赢了')
                pc_win+=1
            choice=input('是否继续猜拳：y：继续 n：退出')
            if choice=='y':
                continue
            else:#按任意键退出
                break
        print('角色赢了{}，电脑赢了{}，平局{}'.format(role_win,pc_win,ping))

if __name__ == '__main__':
    Human_VS_Pc().choose_role()
    # Human_VS_Pc().role_fist()
    # Human_VS_Pc().pc_fist()
    # Human_VS_Pc().role_vs_pc()


