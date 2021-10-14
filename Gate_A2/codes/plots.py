import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp


def x1(t):
    return np.sin(t)

def x2(t):
    return t

def y1 (t): 
    return abs(hilbert(x1(t)))
    
def y2(t):
    return abs(hilbert(x2(t)))
    

def y1plusy2(t):
    return abs(hilbert(np.sin(t)+t))



# Plotting input signals
t = np.linspace(-3 , 3, 100000)
t1 = np.linspace(-10 , 10, 100000)
plt.plot(t, x1(t1) , 'r', label = "$x_1(t) = sin(t)$")
plt.plot(t , x2(t1) , 'b', label = "$x_2(t) = t$")
plt.grid(True)
plt.legend(loc = 'upper right')
plt.title("Input signals")
plt.show()

# Plotting output signals
plt.plot(t , y1(t) , 'r', label = "$\hat{x_1}(t)$")
plt.plot(t , y2(t) , 'b' , label = "$\hat{x_2}(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Output Signals")
plt.show()

# Law of Additivity
plt.plot(t , y1(t) + y2(t) , 'r' , label = "$\hat{x_1}(t) +\hat{x_2}(t)$")
plt.plot(t , y1plusy2(t) , 'k--' , label = "System acting on $x_1(t) + x_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Additivity")
plt.show()

# Law of Homogeneity
plt.plot(t , 2 * y1(t)  , 'r' , label = "$2\hat{x_1}(t)$")
plt.plot(t ,abs(hilbert(2*(x1(t)))) , 'k--' , label = "System acting on $2x_1(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Homogeneity: $k = 2$")
plt.show()

# Time Invariance
# let us introduce a delay of t_0 = 2
plt.plot(t ,  y1(t-2)  , 'r' , label = "$\hat{x_1}(t-t_0)$")
plt.plot(t , abs(hilbert(x1(t-2))), 'k--' , label = "System acting on $x_1(t-t_0)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Time Invariance")
plt.show()
