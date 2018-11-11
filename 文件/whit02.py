import time
with open(r"test01.txt", 'r', encoding='utf-8') as f:
    strChat = f.read(3)
    while strChat:
        print(strChat)
        time.sleep(3)
        strChat = f.read(1)