import matplotlib.pyplot as plt
import numpy as np
def coeff(x,y):
    s_x=np.mean(x)
    s_y=np.mean(y)
    n=np.size(x)
    s=(np.sum(x*y)-n*s_x*s_y)/(np.sum(x*x)-n*s_x*s_x)
    s1=s_y-s*s_x
    return s,s1
x=np.array([2005,2006,2007,2008,2009])
y=np.array([16,19,19,40,45])
plt.scatter(x,y)
p=coeff(x,y)
y_pred=2012*p[0]+p[1]
plt.plot(x,x*p[0]+p[1])

print(y_pred)
plt.show()