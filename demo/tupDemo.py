# -*- codeing = utf-8 -*-
# @author tangwenbo
# @File tupDemo
# @date 2021/2/20 15:45

tup1 = (123, 321, "哈哈哈")
print(tup1)

# 增
tup2 = ("我是第二", "1987")
tip = tup2 + tup1
print(tip)

# 没有改

# 删
del tup1

# 字典
dic1 = {"name": "我是字典", "desc": "跟map一样"}

print(dic1)
print(dic1.get("name", "我是默认值"))

del dic1["desc"]
print(dic1)

dic1["id"] = 123
print(dic1)
dic1["haha"] = 999
print(dic1)
print(dic1.keys())
print(dic1.values())
print(dic1.items())

for key, value in dic1.items():
    print("key=%s,value=%s" % (key, value))
