# _*_ coding:utf-8 _*_
import urllib.request
import urllib.parse


def load_page(url, filname):
    """
        作用：下载需要的页面html
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/63.0.3239.132 Safari/537.36"
    }
    print("正在下载" + filname)
    request = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(request).read()
    html = str(html, encoding='utf8')
    print(html)
    return html


def write_page(html, filename):
    """
        作用：将拿到的页面的html保存到本地
    """
    f = open(filename, 'w', encoding='utf-8')
    f.write(html)
    f.close()


def tieba_spider(url, start_page, end_page, tieba_name):
    """
        作用：对用户输入的参数进行处理
    """
    kw = {"kw": tieba_name}
    kw = urllib.parse.urlencode(kw)
    url = url + kw
    for page in range(start_page, end_page + 1):
        url = url + '&pn=' + str((end_page - start_page) * 50)
        filename = "第" + str(page) + "页.html"
        html = load_page(url, filename)
        write_page(html, filename)


def main():
    tieba_name = input("请输入要爬去的贴吧名字:")
    start_page = int(input("请输入从第几页开始爬："))
    end_page = int(input("请输入爬到第几页："))
    url = "http://tieba.baidu.com/f?"
    tieba_spider(url, start_page, end_page, tieba_name)


if __name__ == '__main__':
    main()
