import urllib.request
import urllib.parse
import re


def load_page(url, start_page, end_page, tieba_name):
    context = {
        'kw': tieba_name
    }
    kw = urllib.parse.urlencode(context)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/63.0.3239.132 Safari/537.36"
    }
    for i in range(start_page, end_page + 1):
        pn = str(50 * (i - 1))
        full_url = url + kw + '&pn=' + pn
        request = urllib.request.Request(full_url, headers=headers)
        html = (urllib.request.urlopen(request).read()).decode('utf-8')
        print('正在处理第' + str(i) + '页')
        html_handle(html)


def html_handle(html):
    pattern = r'<a rel="noreferrer" href="(.*)" title=".*?" target="_blank" class="j_th_tit ">'
    url_list = re.findall(pattern, html)
    count = 1
    for url in url_list:
        print('正在处理第' + str(count) + '个帖子')
        count += 1
        full_url = 'https://tieba.baidu.com' + url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/63.0.3239.132 Safari/537.36"
        }
        request = urllib.request.Request(full_url, headers=headers)
        html = (urllib.request.urlopen(request).read()).decode('utf-8', 'ignore')
        pattern = r'<img class="BDE_Image" .*?src="(.*?)"'
        image_url_list = re.findall(pattern, html)
        write_image(image_url_list)


def write_image(image_url_list):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/63.0.3239.132 Safari/537.36"
    }
    for image in image_url_list:
        filename = image[-10:]
        request = urllib.request.Request(url=image, headers=headers)
        image = (urllib.request.urlopen(request).read())
        print('正在保存图片....')
        with open('图片/' + filename, 'wb') as f:
            f.write(image)


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/f?'
    tieba_name = input("请输入要爬取的贴吧")
    start_page = int(input('请输入要爬取的起始页：'))
    end_page = int(input('请输入要爬取的末尾页：'))
    load_page(url, start_page, end_page, tieba_name)
