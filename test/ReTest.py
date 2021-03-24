# -*- coding = utf-8 -*-
# @author tangwenbo
# @File testRe
# @date 2021/3/3 16:23

import re

pat = re.compile("A")

search = pat.search("我是字符串A")
print(search)
