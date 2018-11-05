class Person():
    name = "lisi"
    __age = 17

print(Person.__dict__)
p = Person()
print(p.__dict__)
