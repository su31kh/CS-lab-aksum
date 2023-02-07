import numpy as np
import matplotlib.pyplot as plt
import math

dt=0.01
DT=(int)(1/dt)

t= np.linspace(0,1,DT)
print(t)

x= (np.exp(t)*(np.sin(4*np.pi*t)-4*np.pi*np.cos(4*np.pi*t))+8*np.pi**2+ 4*np.pi + 0.5)/(np.exp(t)*[1+16*np.pi**2])
#x= np.exp(t+(np.exp(2*t)/2)-0.5)

print(x)
x1= [0.5]

for i in range (1,DT):
    x1.append(x1[i-1]+(-x1[i-1]+ np.sin(4*np.pi*t[i-1]))*dt)

arrx1=np.array(x1)
print(arrx1)
                                                                         
diff= arrx1-x

fig = plt.figure(figsize = (20, 20))                                                   

# plt.plot(t,x) 
plt.plot(t,arrx1)
plt.plot(t,x)

# plt.plot(t,diff)

plt.xlabel("Time")
plt.ylabel("X's value")
plt.legend(["Exact","Euler"])
plt.show()


