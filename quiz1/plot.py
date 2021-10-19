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



import numpy as np
import matplotlib.pyplot as plt


def x1(t):
    return np.sin(t)

def x2(t):
    return t

def x3(t):
    return t**2

def y3 (t): 
    return 2*x3(t)

def y1 (t): 
    return 2*x1(t)
    
def y2(t):
    return 2*x2(t)
    

def y1plusy2(t):
    return 2*(np.sin(t)+t)



# Plotting input signals
t = np.linspace(-10 , 10, 100000)
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
plt.plot(t ,2*(2*(x1(t))) , 'k--' , label = "System acting on $2x_1(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Homogeneity: $k = 2$")
plt.show()

# Time Invariance
# let us introduce a delay of t_0 = 2
plt.plot(t ,  y1(t-2)  , 'r' , label = "$\hat{x_1}(t-t_0)$")
plt.plot(t , 2*(x1(t-2)), 'k--' , label = "System acting on $x_1(t-t_0)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Time Invariance")
plt.show()
