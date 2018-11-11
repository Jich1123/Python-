with open(r"test01.txt",'r', encoding='utf-8') as f:
    strline = f.readline()
    while strline:
        print(strline)
        strline = f.readline()
print("*" * 50)
with open(r"test01.txt",'r', encoding='utf-8') as f:
    l = list(f)
    for i in l:
        print(i)
print("*" * 50)
with open(r"test01.txt", 'r', encoding='utf-8') as f:
    strChat = f.read()
    print(len(strChat))
    print(strChat)
print("*" * 50)
with open(r"test01.txt", 'r', encoding='utf-8') as f:
    strChat = f.read(1)
    print(len(strChat))
    print(strChat)

