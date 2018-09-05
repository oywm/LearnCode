import urllib.request
import ssl
import os
import re


def imageCrawler(url, toPath):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'

    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    # htmlstr = response.read()
    htmlstr = response.read().decode('gbk')
    # with open(r'D:\python工作空间\平时写代码用\爬虫\屌丝爬女装\yhd.html', 'wb') as f:
    #     f.write(htmlstr)

    # <input data-link='http://www.s2tu.com/image/aIL901' data-src='http://www.s2tu.com/images/2018/07/31/1.md.jpg' type='image'>
    pat = r"data-src=(.*?) type="
    re_image = re.compile(pat, re.S)
    imageList = re_image.findall(htmlstr)

    num = 0
    for imageUrl in (imageList):
        imagepath = os.path.join(toPath, str(num) + '.mp4')
        num += 1
        op = urllib.request.build_opener()
        op.addheaders = [
            ('User-Agent',
             'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
             '(KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36')
        ]
        urllib.request.install_opener(op)
        str1 = 'https://www.ppx17.com/get_file/1/819a850faf660b30c61a2f41df2bb5ff/11000/11103/11103.mp4/?br=539&embed=true&rnd=1534140633162'
        urllib.request.urlretrieve(str1, filename=imagepath)


url = 'https://cl.n3s.xyz/htm_data/16/1808/3228601.html'
toPath = 'D:\python工作空间\平时写代码用\爬虫\屌丝爬女装\img1'
imageCrawler(url, toPath)



# 解决urlretrieve 报403错误的
# opener=request.build_opener()
# opener.addheaders=[(‘User-Agent‘,‘Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36‘)]
# request.install_opener(opener)
# request.urlretrieve(url=url,filename=‘%s/%s.txt‘%(savedir,get_domain_url(url=url)))
