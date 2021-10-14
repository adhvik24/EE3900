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
