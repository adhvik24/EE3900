import matplotlib.pyplot as plt
import numpy as np
def u(n):
  if (n >= 0):
    return 1
  else:
    return 0

n = np.linspace(-25,25,51)
n=n.astype(int)
x=np.zeros(51)
for i in range(51):
  x[i] =np.abs(u(n[i])*np.e**(1j*n[i]*(1/8)))


plt.stem(n,x)
plt.grid()
plt.xlabel("n")
plt.ylabel("|x[n]|")

plt.show()

n = np.linspace(-25,25,51)
n=n.astype(int)
x=np.zeros(51)
for i in range(51):
  x[i] =np.angle(u(n[i])*np.e**(1j*n[i]*(1/8)))

plt.stem(n,x)
plt.grid()
plt.xlabel("n")
plt.ylabel("arg(x[n])")

plt.show()


n = np.linspace(-25,25,51)
n=n.astype(int)
x=np.zeros(51)
for i in range(51):
  x[i] =np.abs(2*u(n[i])*np.e**(1j*n[i]*(1/8)))


plt.stem(n,x)
plt.grid()
plt.xlabel("n")
plt.ylabel("|y[n]|")

plt.show()

n = np.linspace(-25,25,51)
n=n.astype(int)
x=np.zeros(51)
for i in range(51):
  x[i] =np.angle(2*u(n[i])*np.e**(1j*n[i]*(1/8)))

plt.stem(n,x)
plt.grid()
plt.xlabel("n")
plt.ylabel("arg(y[n])")

plt.show()
