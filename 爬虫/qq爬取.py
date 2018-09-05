import urllib.request
import os
import ssl
import re


# D:\python工作空间\平时写代码用\爬虫\qq
def writeFileBytes(htmlBytes, toPath):
    with open(toPath, 'wb') as f:
        f.write(htmlBytes)


def writeFileStr(htmlBytes, toPath):
    with open(toPath, 'w') as f:
        f.write(htmlBytes.decode('utf-8'))


def getHtmlBytes(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()

def qqCrawler(url, toPath):
    htmlBytes = getHtmlBytes(url)
    # writeFileBytes(htmlBytes, toPath)
    htmlStr = str(htmlBytes.decode('utf-8'))

    # <p class="">是喜欢爬山，但这个头像也能看出来吗？</p>
    #    <a href="/tel/01065961114/">外交部</a>   [\u4e00-\u9fa5]
    pat = r'<a href="/tel/(\d*)/">(.*?)</a>'
    qqsList = re.findall(pat, htmlStr, re.S)
    # re_qq = re.compile(pat)
    # qqsList = re_qq.findall(htmlStr)
    qqsList = list(set(qqsList))

    tel = ''
    for item in qqsList:
        phone, name = item
        tel += name+':'+phone+'\n'

    tel = bytes(tel, encoding='utf-8')
    writeFileStr(tel, toPath)


url = r'http://www.114best.com/tel/'
toPath = r'D:\python工作空间\平时写代码用\爬虫\qq\qqFile.txt'
qqCrawler(url, toPath)

