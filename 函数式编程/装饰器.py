import time
# 定义装饰器
def printCurTime(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())
        time.sleep(1)
        return f(*args,**kwargs)
    return wrapper

# 使用装饰器
@printCurTime
def hello():
    print("Hello World!")

hello()
hello()
hello()
print("* " * 20)
# 手动加载装饰器
def hello1():
    print("手动执行")
funA = printCurTime(hello1)
funA()