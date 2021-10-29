
import numpy as np
import matplotlib.pyplot as plt
import seaborn
#seaborn.set(style='ticks')

fig, ax = plt.subplots()
x=np.linspace(-80,80,160)

y=1/((np.pi)*x)
plt.plot(x,y,color='blue',label="impulse response h(t)")
#ax.set_aspect('equal')
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
ax.grid(True, which='both')
#seaborn.despine(ax=ax, offset=0) 
plt.legend(loc = 'upper right')
plt.show()
x=np.linspace(-8,8,160)

y=1/((np.pi)*x)
fig, ax = plt.subplots()
fourier=np.fft.fft(y)
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
freq=np.fft.fftfreq(fourier.shape[0], d=1/1e5)
plt.plot(freq, np.abs(fourier))
plt.xlabel('$f$')
plt.ylabel('$A$')
plt.show()
plt.plot(freq, (fourier),color='y')
plt.show()
fig, ax = plt.subplots()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.plot(freq, np.angle(fourier))
plt.xlabel('$f$')
plt.ylabel('$\phi$')
plt.show()
import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 6, 3

N = 500
x = np.linspace(-80,80, N)

def sgn(t):
    y = np.zeros(N)
    for i in range(N):
        if t[i] > 0:
            y[i] = 1
        if t[i] == 0:
            y[i] = 0
        if t[i] < 0:
            y[i] = -1
    return y
#Computing the rectangular function
y1 = sgn(x)/1j

plt.plot(x, np.abs(y1))
plt.xlabel('$t$')
plt.ylabel('$A$')
plt.grid()
plt.show()

plt.plot(x, np.angle(y1))
plt.xlabel('$t$')
plt.ylabel('$\phi$')
plt.grid()
plt.show()
