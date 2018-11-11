import shelve
with shelve.open(r"test04.db", writeback=True) as shv:
    sk = shv["one"]
    print(sk)
    sk["one"] = 1000

with shelve.open(r"test04.db") as shv:
    print(shv["one"])
