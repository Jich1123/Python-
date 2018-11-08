l1 = [1,4,2,7,5,8,9,0,14]
print(l1)
l2 = sorted(l1)
print(l2)
l3 = sorted(l1,reverse=True)
print(l3)

l4 = [-123,72,-23,88,2,10]
l5 = sorted(l4,key=abs,reverse=True)
print(l5)

l6 = ['A','a','D','C','d']
l7 = sorted(l6)
print(l7)
l8 = sorted(l6,key=str.lower,reverse=True)
print(l8)