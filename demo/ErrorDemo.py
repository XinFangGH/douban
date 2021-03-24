# -*- codeing = utf-8 -*-
# @author tangwenbo
# @File ErrorDemo
# @date 2021/2/23 15:14

#
# try:
#     print("------我是第一行-------")
#     import os
#     os.mkdir("/error")
#
# except Exception as r:
#     print("错误发生了")
#     print(r)
#
# finally:
#     print("我是最终执行的")


w = open("gushi.txt", "w")
w.write("     白雪歌送武判官归京\n")
w.write("                作者：岑参\n")
w.write("北风卷地白草折，胡天八月即飞雪。\n")
w.write("忽如一夜春风来，千树万树梨花开。\n")
w.write("散入珠帘湿罗幕，狐裘不暖锦衾薄。\n")
w.write("将军角弓不得控，都护铁衣冷难着。\n")
w.write("瀚海阑干百丈冰，愁云惨淡万里凝。\n")
w.write("中军置酒饮归客，胡琴琵琶与羌笛。\n")
w.write("纷纷暮雪下辕门，风掣红旗冻不翻。\n")
w.write("轮台东门送君去，去时雪满天山路。\n")
w.write("山回路转不见君，雪上空留马行处。\n")
w.close()


def copyTxt(txtName):
    r = open(txtName, "r")
    readlines = r.readlines()
    copy = open("copy.txt", "w")
    for readline in readlines:
        copy.write(readline)

    print("复制完毕")


copyTxt("gushi.txt")
