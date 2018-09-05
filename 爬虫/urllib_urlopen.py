# _*_ coding:utf-8 _*_
import urllib.request

request = urllib.request.Request('http://www.baidu.com/')
response = urllib.request.urlopen(request)
html = response.read()
data = str(html, encoding='utf-8')
print(data)


