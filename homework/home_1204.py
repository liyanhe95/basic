# 1：有a和b两个列表如下所示：
a=[1,2,3,"this is a list"]
b=[4,5,6,"这是第二个列表"]
# 1:把a 和b的值一起组合打印出来
a.extend(b)
print(a)
# 2：输出列表a两次
print(a*2)
# 3：取a列表第一个值
print(a[0])
# 4：取a列表第二个和第三个值
print(a[2:4])
# 5：取a列表第三个值以及到末尾的所有值
print(a[3:])
#
# 2：
L = [['Apple', 'Google', 'Microsoft'],['Java', 'Python', 'Ruby', 'PHP'],['Adam', 'Bart', 'Lisa']]
# 打印Apple、Python、Lisa
print(L[0][0],L[1][1],L[2][2])
# 3.合并下面的两个list并去重（去重可以使用set函数）
list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
list1.extend(list2)
print(set(list1))