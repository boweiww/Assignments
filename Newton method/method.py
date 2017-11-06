import math
def f(m):
    y=m*(math.pow(1.06,20)-1)/0.06-100000*math.pow(1.06,20)
    print "f(x) = "+str(y)
    return y
def fd(m):
    y= (math.pow(1.06,20)-1)/0.06
    print "f'(x)= "+ str(y)
    return y

x=[10000]*11

for k in range(10):
    x[k+1]=x[k]-f(x[k])/fd(x[k])
    print x[k+1]
