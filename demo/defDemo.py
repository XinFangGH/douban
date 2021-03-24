# -*- codeing = utf-8 -*-
# @author tangwenbo
# @File defDemo
# @date 2021/2/23 14:23

# 函数调用

def printUtil():
    print("~~~~~~~~~~~~~~~")
    print("我是一个函数调用")
    print("我是一个函数调用")
    print("~~~~~~~~~~~~~~~")


printUtil()

print()


def addNum(a, b):
    print((a + b))


addNum(3, 4)
print()


def returnNum(a, b):
    return a + b


num = returnNum(1, 3)
print(num)
print()


def return2Num(a, b):
    c = a + b
    d = a * b
    return c, d


he, ji = return2Num(3, 4)
print(he, ji)
print()


def drawLine(a):
    for b in range(a):
        print("%s-------------------" % b)


drawLine(10)
print()


def sum_3_num(a, b, c):
    print(a + b + c)
    return a + b + c


def avg_3_num(a, b, c):
    sumNum = sum_3_num(a, b, c)
    print(sumNum / 3)
    return sumNum / 3


avg_3_num(1, 2, 3)
print()

base = 100
print(base)

def updateBase():
    global base
    base = 200

def updateBase2():
    base = 300

updateBase()
print(base)
print()

updateBase2()
print(base)
print()