from urllib import request
from bs4 import BeautifulSoup
url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()
soup = BeautifulSoup(content,'lxml')
content = soup.prettify()
# print(content)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])
soup.link.attrs['type'] = "jich"
print(soup.link)
print("*" * 30)
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print("*" * 30)
print(soup.name)
print(soup.attrs)
print(soup.name)
print("*" * 30)
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node.string)
print("*" * 30)
import re
tags = soup.find_all(name="meta")
print(tags)
print("*" * 30)
tags = soup.find_all(re.compile(r'^me'), content="always")
for tag in tags:
    print(tag)

