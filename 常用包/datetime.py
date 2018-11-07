from datetime import datetime,timedelta
'''
print(datetime.date(2018,11,8))
dt = datetime.date(2018,2,1)
print(dt.year,dt.month,dt.day)
'''
t1 = datetime.now()
print(t1.strftime("%Y%m%d %H:%S"))
td = timedelta(hours=1)
print((t1+td).strftime("%Y%m%d %H:%S"))