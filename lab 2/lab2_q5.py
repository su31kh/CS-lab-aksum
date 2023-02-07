import numpy as np
import matplotlib.pyplot as plt
import math

dt=0.01
DT=(int)(1/dt)

t= np.linspace(0,1,DT)
print(t)

x= (t+0.1)/(np.exp(2*t))

print(x)
x1= [0.1]

for i in range (1,DT):
    x1.append(x1[i-1]+(-2*x1[i-1]+ np.exp(-2*t[i-1]))*dt)

arrx1=np.array(x1)

print(arrx1)

diff= x-arrx1

fig = plt.figure(figsize = (10, 10))

plt.plot(t,x) 
plt.plot(t,arrx1)

# plt.plot(t,diff)

plt.xlabel("Time")
plt.ylabel("X's value")
plt.legend(["Exact","Euler"])
plt.show()


