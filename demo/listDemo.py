# -*- codeing = utf-8 -*-
# @author tangwenbo
# @File listDemo
# @date 2021/2/20 14:51


nameList = ["张三", "jack", "李四", 123321]
print(nameList)

nameList.append("xixixi")
print(nameList)

nameList.pop()
print(nameList)
# 插入
bName = ["第二个", "第二"]
nameList.append(bName)
print(nameList)

nameList.extend(bName)
print(nameList)

nameList.insert(0, "我是第一!")
print(nameList)
# 删除
del nameList[0]
print(nameList)

nameList.append("重复数据")
nameList.append("重复数据")
print(nameList)

nameList.remove("重复数据")
print(nameList)
# 改
nameList[0] = "我修改了张三"
print(nameList)

# 查
# findName = input("请输入需要查找的内容:")
# if findName in nameList:
#     print("恭喜你找到了", findName)
# else:
#     print("没找到啊兄弟")

# ~~~~~~~~~~~~~~~~~~
print()
print()

productList = [["iphone", "6888"], ["MacPro", "14800"], ["Mi 11", "3999"],
               ["Book", "33"], ["Nike", "699"], ["Anta", "399"]]
print("`````````商品列表`````````")

for index, product in enumerate(productList):
    print(index, end="\t")
    for name in product:
        print(name, end="\t")
    print()

buyCar = []
while True:
    id = input("请输出需要购买的商品编号:")
    if id != "q":
        buyCar.append(productList[int(id)])
        print("恭喜%s号商品加入购物车成功" % id)
    else:
        print("结束购物,请查看您的购物车明细")
        break

for car in buyCar:
    print(car)
