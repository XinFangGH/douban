# -*- coding = utf-8 -*-
# @author tangwenbo
# @File XwltTest
# @date 2021/3/23 17:49
import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
sheet = workbook.add_sheet("sheet1")

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            sheet.write(j - 1, i - 1, "%d*%d=%d" % (i, j, i * j))
workbook.save("demo.xls")
