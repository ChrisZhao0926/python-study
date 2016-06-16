
from __future__ import division
def add(x,y):
    return x+y

def sub(x,y):
    return x-y
    
def mul(x,y):
    return x*y
    
def div(x,y):
    return x/y
    
operator={"+":add,"-":sub,"*":mul,"/":div}

# print operator["+"]
# print add
# print operator["+"](3,4)

def oper(x,o,y):
    print operator.get(o)(x,y)
    
