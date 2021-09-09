import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10, 3, 100)

#Calculate the y value for each element of the x vector
y = x**2 + 7*x + 10
a = 1
b = 7
c = 10

d1 = -b + np.sqrt(b**2-4*a*c)
d2 = -b - np.sqrt(b**2-4*a*c)
d1 = d1/(2*a)
d2 = d2/(2*a)
print('The solutions of the equations are',d1,'and',d2)

#Plotting
fig, ax = plt.subplots()
ax.plot(x, y)

plt.plot(d2,0, 'o')
plt.text(d2,0.5, 'D')
plt.plot(d1, 0, 'o')
plt.text(d1,0.5, 'E')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.show()
