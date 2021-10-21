import numpy as np
import matplotlib.pyplot as plt

def u(x):
    res = []
    for i in range(len(x)):
        if x[i] >=0 :
            res.append(1)
        else:
            res.append(0)
    return res



n, radii = 50, [1]
pole1 = [-1,0]
zero = [1,0]

theta = np.linspace(0, 2*np.pi, n, endpoint=True)
xs = np.outer(radii, np.cos(theta))
ys = np.outer(radii, np.sin(theta))

# in order to have a closed area, the circles
# should be traversed in opposite directions
xs[0,:] = xs[0,::-1]
ys[0,:] = ys[0,::-1]

ax = plt.subplot(111, aspect='equal')
plt.plot(np.sin(theta), np.cos(theta) , 'k-' , label = "Unit Circle: $|z| = 1$")
plt.plot([pole1[0]] , [pole1[1]] , 'rx' , label = "Poles of $H(z)$")
plt.plot(zero[0],zero[1] , 'ro' , label = "Zeroes of $H(z)$")
plt.title("Pole-Zero Plot with ROC")
plt.grid(True)
plt.legend(loc='upper right',fontsize=9)
plt.show()
