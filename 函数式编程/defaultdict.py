from collections import defaultdict
func = lambda : "Jich"
d = defaultdict(func)
d["one"] = 1
d["tow"] = 2
print(d["one"])
print(d["four"])