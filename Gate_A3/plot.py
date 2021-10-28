import matplotlib.pyplot as plt
import numpy as np
def y(t):
  arr = []
  for i in range(1000):
    if (t[i] >= 4 or t[i]<0):
      arr.append(0)
    if(t[i]>=0 and t[i]<1):
      arr.append(-t[i])
    if(t[i]>=1 and t[i]<2):
      arr.append(3*t[i]-4)
    if(t[i]>=2 and t[i]<3):
      arr.append(8-3*t[i])
    if(t[i]>=3 and t[i]<4):
      arr.append(t[i]-4)
  return arr

def u(t):
  arr = []
  for i in range(1000):
    if (t[i] >= 0):
      arr.append(1)
    else:
      arr.append(0)
  return arr

n = np.linspace(-1,3,1000)

x= np.array(u(n))-2*np.array(u(n-1))+np.array(u(n-2)) 
h = -np.array(u(n))+2*np.array(u(n-1))-np.array(u(n-2)) 
plt.plot(n,x,label="x(t)")
plt.grid(True)
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.legend(loc = 'upper right')
plt.title("Input signal")
plt.show()

plt.plot(n,h,label="h(t)")
plt.grid(True)
plt.xlabel('$t$')
plt.ylabel('$h(t)$')
plt.legend(loc = 'upper right')
plt.title("impulse response of matched filter")
plt.show()

n = np.linspace(-2,6,1000)

plt.plot(n,y(n),label="y(t)")
plt.grid(True)
plt.xlabel('$t$')
plt.ylabel('$y(t)$')
plt.legend(loc = 'upper right')
plt.title("output signal")
plt.show()

