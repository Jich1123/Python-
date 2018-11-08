def myFun1():
    def myFun2():
        print("This is myFun2")
        return 2
    return myFun2

myFun3 = myFun1()
print(type(myFun3))
myFun3()

def FunA(*args):
    def FunB():
        l = 0
        for i in args:
            l += i
        return l
    return FunB
FunC = FunA(1,2,3,4,5,6,7)
print(FunC())
FunD = FunA(1,2,3,4)
print(FunD())
