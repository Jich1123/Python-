#coding=utf-8
from io import open
with open(u"百度贴吧.txt", 'r', encoding='utf-8') as f:
    pos = f.tell()
    strChat = f.read(3)
    while strChat:
        # print(pos)
        print(strChat)
        pos = f.tell()
        strChat = f.read(3)