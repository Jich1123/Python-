import collections
Point = collections.namedtuple("Point",['x','y'])
p = Point(11,22)
print(p.x)
print(p[0])

Circle = collections.namedtuple("Circle",['x','y','r'])
c = Circle(10,20,30)
print(c)
print(type(c))
print(isinstance(c,tuple))