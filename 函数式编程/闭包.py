# 坑
def count():
    ls = []
    for i in range(1,4):
        def funA():
            return i * i
        ls.append(funA)
    return ls
a,b,c = count()
print(a())
print(b())
print(c())

# 修改
def count2():
    def Temp(j):
        def FunA():
            return j*j
        return FunA
    ls = []
    for i in range(1,4):
        ls.append(Temp(i))
    return ls
a,b,c = count2()
print(a())
print(b())
print(c())