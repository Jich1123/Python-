def isEvn(n):
    return n % 2 == 0
l1 = [1,2,3,4,5,6,7,8,9,10]
rst = filter(isEvn,l1)
print(type(rst))
print(rst)
print(list(rst))