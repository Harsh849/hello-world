import numpy as np
def trapezoidal(n):
    def f(x):
        return np.sin(x)
    a=0
    b=np.pi
    delx=(b-a)/n
    sum=0
    sum3=delx*((f(a)+f(b))/2)
for i in range(n):
        x1=a+i*delx
        sum=sum+f(x)*delx

print(sum+sum3, "by trapezoidal")

