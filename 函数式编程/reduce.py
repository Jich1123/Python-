from functools import reduce
def fn(x,y):
    return x + y

rst = reduce(fn,[1,2,3,4,5,6,7])
print(rst)