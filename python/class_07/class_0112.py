import json  #josn 模块处理字符串和json之间的转换
#为什么把字符串转换成json
#loads 字符串转成字典
#dumps dict转成字符串 None
#python dict字符串用单引号，json强制规定用双引号
#python dict里可以嵌套tuple，json里只有array。json.dumps({1:2})的结果是{"1":2}
#
# d_2 = '{"status":1,"code":"10001","data":null,"msg":"登录成功"}'
# print(type(json.loads(d_2)))
# print(json.loads(d_2))

#json.loads(str)--->json 格式的字符串转成字典
#None null null --None json.loads(str)
#json--dict json里面的键值对必须都是双引号
#python --None
#json  --null
# #python中没有null，只支持None
# d_1 = {"status":1,"code":"10001","data":None,"msg":"登录成功"}
# print(type(d_1))
# # #json.dumps(str)--->dict 转成json格式的字符串
# print(json.dumps(d_1))