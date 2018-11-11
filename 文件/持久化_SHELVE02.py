import shelve
shv = shelve.open(r'test04.db')
try:
    shv["one"] = {"one":1,"two":2}
    print(shv["one"])
except Exception as e:
    print("出错了")
finally:
    shv.close()

shv = shelve.open(r'test04.db',writeback=True)
try:
    sk1= shv["one"]
    print(sk1)
    sk1["one"] = 100
except Exception as e:
    print("出错了")
finally:
    shv.close()

shv = shelve.open(r'test04.db')
try:
    print(shv["one"])
    print(shv["name"])
except Exception as e:
    print("出错了")
finally:
    shv.close()

