import urllib.parse
import urllib.request

headers = {
    "User-Agent": "Mozilla...."
}
url = 'http://www.baidu.com/s'
key_word = input('请输入需要查询的关键字：')
wd1 = {'wd': key_word}
wd = urllib.parse.urlencode(wd1)
full_url = url + '?' + wd

request = urllib.request.Request(full_url, headers=headers)

response = urllib.request.urlopen(request)
html = str(response.read(), encoding='utf-8')
print(html)
