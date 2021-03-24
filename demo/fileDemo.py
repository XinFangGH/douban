# -*- codeing = utf-8 -*-
# @author tangwenbo
# @File fileDemo
# @date 2021/2/23 14:54

# 打开文件,文件不存在就新建(w)
# f = open("fileDemo.txt", "w")
#
# f.write("测试一下当前是否新建成功")
#
# f.close()

# 读取文件
r = open("fileDemo.txt", "r")

# readline = r.readline()  # 读取当前行
# print(readline)
readlines = r.readlines()  # 读取所有行
print(readlines)
r.close()


import os
# os.mkdir("file")

os.removedirs("file")