#print(int("xvf"))
def a(var):
    try:
        return int(var)
    except ValueError as Argument:
        print(Argument)

a("zvf")
