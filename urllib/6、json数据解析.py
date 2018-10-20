'''

概念：一种保存数据的格式
作用：可以保存本地的json文件，也可以将json串进行传输，通常将json称为轻量级的传输方式

xml可读性更强，但是有很多没有用的标签

json文件组成：
{}		代表对象（字典）
[]		代表列表
:		代表键值对
,		分隔两个部分


'''

import json

# 将json格式的字符串转换为Python数据类型的对象

jsonStr = '{"name":"xiaoxiao", "age":18, "hobby":["money", "power", "english"], "parames":{"a":1, "b":2}}'

jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(jsonData["hobby"])


jsonData2 = {"name": "xiaoxiao", "age": 18, "hobby": [
    "money", "power", "english"], "parames": {"a": 1, "b": 2}}
# python类型的数据就是比json格式少个引号

# 将Python数据类型的对象转换为json格式的字符串

jsonStr2 = json.dumps(jsonData2)
print(jsonStr2)
print(type(jsonStr2))
