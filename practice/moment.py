
import inspect

def callfuction():
    return inspect.stack()[1][3]

def myfunc():
    x=callfuction()
    print(x)

myfunc()