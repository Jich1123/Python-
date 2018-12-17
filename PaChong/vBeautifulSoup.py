import bs4
from bs4 import BeautifulSoup

html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

soup = BeautifulSoup(html_doc, 'lxml')
find = soup.find('p')
print("find's return type is ", type(find))  #输出返回值类型
print("find's content is", find)  #输出find获取的值
print("find's Tag Name is ", find.name)  #输出标签的名字
print("find's Attribute(class) is ", find['class'])  #输出标签的class属性值


print(soup.find_all("title"))
print(soup.find_all("p", "title"))
print(soup.find_all("a"))
print(soup.find_all(id="link2"))

import re
print(soup.find(string=re.compile("sisters")))


print(soup.find('title'))
print(soup.find("head").find("title"))


# print('NavigableString is：', find.string)
# print("* " * 50)
# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
# soup = BeautifulSoup(markup, 'lxml')
# comment = soup.b.string
# print(comment)
# print(type(comment))
# if type(comment) == bs4.element.Comment:
#     print('该字符是注释')
# else:
#     print('该字符不是注释')

