# -*- codeing = utf-8 -*-
# @author tangwenbo
# @File forDemo
# @date 2021/2/19 18:14

def demo123(var):
    print("调用方法", var)


for a in range(0, 10, 5):
    print(a)

c = "中国"
for b in c:
    print(b)

for i in range(1, 10):
    for x in range(1, i + 1):
        print("%d*%d=%d" % (i, x, i * x), end="\t")
    print()

demo123(2)
