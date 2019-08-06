#局部变量
#全局变量
#湖南都是晴天 除了长沙是雨天
#全局变量:晴天
#局部变量:雨天
#全局变量生效的范围大于局部变量
#当局部变量存在的时候，
#python 里面的全局和局部
#函数外的是 全局变量
#函数内的是 局部变量
offer = 1
# offer = None #存最高offer
def student_info(class_name,name):   #调用student_info 才会设计修改offer的值
    global offer  # 声明全局变量
    offer=20  #局部变量  在函数内部生效
    print('{}期的{}同学拿到了{}k的offer!!!恭喜恭喜'.format(class_name,name,offer))

def student_record(): #记录最高薪资
    # offer=18
    print('目前柠檬班的最高薪资是{}k'.format(offer))

student_info('python','li')
print(offer)
student_record()

#当全局变量和局部变量同时存在的时候，优先取局部变量
#global  全局变量
#使用场景：两个请求同时用了一个变量，如果第二个请求用的是第一个请求改变过后的变量值