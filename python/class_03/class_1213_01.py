def student_info(class_name,name,offer):
    print('{}期的{}同学拿到了{}k的offer!!!恭喜恭喜'.format(class_name,name,offer))
    eat('玉米','可乐')

def eat(*args): #动态参数
    food_name= ''  #存储我放进来的食物
    # for item in range(len(args)):
    #     food_name+=args[item]
    #     if item!=len(args)-1:
    #         food_name += '、'
    for item in args:
        food_name+=item
        food_name+='、'
    food_name=food_name.strip('、')
    print('最喜欢吃:{}'.format(food_name))

#测试代码
#你不想影响别的模块调用这个文件，执行代码放到main下面
if __name__ == '__main__':
    #代码执行的入口，只会在当前模块中运行代码的时候，执行下面的代码
    student_info('python13','litongxue','18')
    eat('煎饼','玉米','火锅','泡面')