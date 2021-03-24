# -*- coding = utf-8 -*-
# @author tangwenbo
# @File UrllibTest
# @date 2021/3/2 17:45


import urllib.request
import urllib.response
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=100)
#     print(response.read().decode("utf-8"))
# except Exception as e:
#     print("超时了,原因:%s" % e)

# post请求
# response = urllib.request.urlopen("http://httpbin.org/post", data=bytes("hello", encoding="utf-8"))
# print(response.read().decode("utf-8"))


url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}
# data = bytes("hello world", encoding="utf-8")
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
