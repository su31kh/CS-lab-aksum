import numpy as np
import matplotlib.pyplot as plt
import math

dt=0.01
DT=(int)(1/dt)

t= np.linspace(0,1,DT)
print(t)

x=  t*t - 2*(t-1) -(1/np.exp(t))

print(x)
x1= [1]

for i in range (1,DT):
    x1.append(x1[i-1]+(-1*x1[i-1]+ t[i-1]**2)*dt)

arrx1=np.array(x1)
print(arrx1)

diff= x-arrx1

fig = plt.figure(figsize = (8, 10))

# plt.plot(t,x) 
# plt.plot(t,arrx1)

plt.plot(t,diff)

plt.xlabel("Time")
plt.ylabel("X's value")
plt.legend(["Exact","Euler"])
plt.show()


