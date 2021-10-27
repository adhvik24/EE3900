import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='ticks')

x = np.linspace(0.2,10,100)
fig, ax = plt.subplots()
x=np.linspace(1,80)
x1=np.linspace(-80,80)
y1=x1*0
y=1/((np.pi)*x)
plt.plot(x,y,color='blue',label="impulse response h(t)")
plt.plot(-x,-y,color='blue')
#ax.set_aspect('equal')
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
ax.grid(True, which='both')
seaborn.despine(ax=ax, offset=0) 
plt.legend(loc = 'upper right')
plt.show()
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
