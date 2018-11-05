class Person():
    name = "NoName"
    age = 10
    _per_name = "sec"
    def __init__(self):
        print("I am a person")
    def work(self):
        print("make nore manry")

class Teacher(Person):
    def __init__(self):
        print("I am a teacher")
    def work(self):
        super().work()
        print("i can leran")

class Student(Person):
    pass

t = Teacher()
t.work()
s = Student()
s.work()
print(Student.__mro__)
