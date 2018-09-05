from bs4 import BeautifulSoup as bf

html_doc = """
<html><head><title name='haha'>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bf(html_doc, 'lxml')

# soup.prettify()将html转化位格式化的html
# print(soup.prettify())

# 查看html中第一个title标签
# print(soup.title)

# 查看title标签的名字
# print(soup.title.name)

# 查看title标签的所包含的文档内容
# print(soup.title.string)

# soup.p['class']获取html文件的第一个p标签下class属性的值
# print(soup.p['class'])

# 找到所有的a标签
# print(soup.find_all('a'))

# 从文档中找到所有<a>标签的链接:
for link in soup.find_all('a'):
    print(link.get('href'))

# 从文档中获取所有的文字内容
print(soup.text)