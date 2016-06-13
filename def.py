
# def fun():
#     if True:
#         print "good"
        
# fun()


def fun(*args):
    print args
    for i in args :
        print i
    
fun(1,2,3)

def fun1(**kwargs):
    print kwargs

fun1(x=1,y=2)