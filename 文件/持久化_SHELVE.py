import shelve
'''
shv = shelve.open(r'test04.db')
shv["name"] = "Jich"
shv["age"] = 18
shv.close()
'''

shv1 = shelve.open(r'test04.db')
try:
    print(shv1["name"])
    print(shv1["age123"])
except Exception as e:
    print("出错了")
finally:
    shv1.close()
