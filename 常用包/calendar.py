import calendar
car = calendar.calendar(2018)
print(type(car))
print(car)

help(calendar.leapdays)
print(calendar.__doc__)

m11 = calendar.month(2018,11)
print(m11)

wt = calendar.monthrange(2018,11)
print(wt)
w,t = calendar.monthrange(2018,11)
print(w,t)
help(calendar.monthrange)