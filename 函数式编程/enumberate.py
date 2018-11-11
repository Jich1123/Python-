l1 = [1,2,3,4,5]
em = enumerate(l1)
l2 = [i for i in em]
print(l2)

em1 = enumerate(l1,start=100)
l3 = [i for i in em1]
for i in l3:
    print(i)