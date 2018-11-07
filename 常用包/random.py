import random
print(int(random.random()*100))
l = [str(i)+"Jich" for i in range(20)]
rst = random.choice(l)
print(rst)
l1 = [i for i in range(10)]
print(l1)
random.shuffle(l1)
print(l1)
print(random.randint(1,100))