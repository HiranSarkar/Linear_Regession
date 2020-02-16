import matplotlib.pyplot as plt
import numpy as np
def loss(x,y,s,s1):
    z=0.0
    a=0.0
    q=float(len(x))
    for i in range (len(y)):
        z+=((y[i]-(s*x[i]+s1))*x[i])/q
        a+=(y[i]-(s*x[i]+s1))/q
    return [-z,-a]
def coeff(x,y,iter):
    s=0.0
    s1=0.0
    c=loss(x,y,s,s1)
    for i in range(iter):
        s=s-0.001*c[0]
        s1=s1-0.001*c[1]
        c=loss(x,y,s,s1)
    return s,s1
x=np.array([5,6,7,8,9])
y=np.array([12,19,29,37,45])
plt.scatter(x,y)
iter=100000
p=coeff(x,y,iter)
print(p)
plt.plot(x,x*p[0]+p[1])
plt.show()