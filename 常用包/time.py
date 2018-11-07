import time
'''
print(time.timezone/3600)
print(time.time())
t = time.localtime()
print(t)
print(t.tm_yday)

for i in range(10):
    print(i)
    time.sleep(0.2)

def p():
    time.sleep(2.5)
t0 = time.perf_counter()
p()
t1 = time.perf_counter()
print(t0 - t1)
'''
t = time.localtime()
print(t)
ft = time.strftime("%Y%m%d %H:%M" , t)
print(ft)