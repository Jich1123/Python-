l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i * 10)
print(l2)
def fn(n):
    return n * 10
l3 = map(fn,l1)
#help(map)
for i in l3:
    print(i,end=" ")
print()
l4 = [i for i in l3]
print(l4)