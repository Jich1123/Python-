with open(r"test01.txt", 'r', encoding='utf-8') as f:
    pos = f.tell()
    strChat = f.read(3)
    while strChat:
        print(pos)
        print(strChat)
        pos = f.tell()
        strChat = f.read(3)