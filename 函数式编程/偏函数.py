import functools
def int16(x,base=16):
    return int(x,base=base)
print(int16("12345"))

int160 = functools.partial(int,base=16)
print(int160("12345"))