import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

dt = 0.05
DT = 1 / dt

print(dt,DT)


def returns_dydt(y,t):
	# dydt = -y
	dydt = (-1)*y*y
	return dydt

# initial condition
y0 = 1

# values of time
t = np.linspace(0, 1, int(DT) + 1)

# solving ODE
y = odeint(returns_dydt, y0, t)
print(y)




def fn(x):
    # return -x
	return (-1)*x*x

def euler(x0):

    # x(n+) = x(n) - x(n)*dt
    ans = []
    # ans.append(x0*(1 - dt))
    ans.append(x0)
    # for i in range(1,100):
    for i in range(1,int(DT)):
        ans.append(ans[i-1] + dt*fn(ans[i-1]))
    return ans

def erer(ans):
    errr = []
    errr.append(0)
    for i in range(1,int(DT)):
        # errr.append(100*((ans[i] - np.exp((-1) * i * dt)) / np.exp((-1) * i * dt)))
        # errr.append(((ans[i] - np.exp((-1) * i * dt)) / np.exp((-1) * i * dt)))
        errr.append(((ans[i] - float(y[i]))))
    return errr
    
    

# ans = euler(0.01, 1)
ans = euler(1)
errr = erer(ans)
print(ans)
print(errr)
# print(ans, errr)
x = np.linspace(0, 1, int(DT))


 
# fig = plt.figure(figsize = (10, 5))


# Create the plot

plt.plot(x, errr, color = 'green', label = '0.05', linewidth=5)
# plt.title("Q1 exact")
# plt.xlabel('t')
# plt.ylabel('x(t) = e^(-t)')
# plt.ylim(-0.01,0)
# plt.xlim(0, 1)

 
# Show the plot
plt.legend()
plt.grid()
plt.show()