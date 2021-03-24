# -*- coding = utf-8 -*-
# @author tangwenbo
# @File testBs4
# @date 2021/3/3 15:34

from bs4 import BeautifulSoup
import urllib.request
import re

url = "http://www.baidu.com"

html = urllib.request.urlopen(url).read().decode("utf-8")

bs = BeautifulSoup(html, "html.parser")

# Tag 标签及其内容,只展示第一个出现的标签里所有信息<div></div>
# print(bs.div)

# NavigableString 获取标签里面的字符串内容
# print(bs.title.string)

# BeautifulSoup 表示整个文档
# print(bs)

# comment 是一个特殊的NavigableString,输出的时候不包含注释信息
# print(bs.a.string)

# 遍历文档
# print(bs.div.contents[3])

# 文档的搜索

# find_all()  查询所有
# print(bs.find_all("a"))

# 正则表达式搜索
# print(bs.find_all(re.compile("a")))

# 按照自定义函数方法搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# print(bs.find_all(name_is_exists))


# kwargs 参数
# print(bs.find_all(id="123"))
# print(bs.find_all(text=["新闻", "你就知道"]))  # 文本内容查找
# print(bs.find_all(text=re.compile("\\d")))   # 正则表达式查找

# css选择器查找

print(bs.select("title"))  # 通过标签查找
print(bs.select(".mnav"))  # 通过类名查找
print(bs.select("#u1"))  # 通过id查找
print(bs.select("a[class='s-top-right']"))  # 通过属性查找
print(bs.select("head > title"))  # 通过子标签查找
print(bs.select(".mnav ~ .bri"))  # 通过兄弟同级标签查找
