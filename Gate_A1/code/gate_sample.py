import numpy as np
import matplotlib.pyplot as plt
# Let f_s be 25.
f_s = 25
t1 = np.linspace(-18 ,-5 ,10)
t2 = np.linspace( -5 , 0 ,10)
t3 = np.linspace( 0 , 5 , 10 )
t4 = np.linspace( 5 , 18 , 10 )
x1=t1*0
x2=t2 +5
x3=-t3+5
x4=t4*0
# x(t)
x = np.concatenate(( x1 , x2 , x3 , x4 ),axis = 0)
t=np.concatenate(( t1 , t2  , t3 , t4),axis = 0)
t110 = np.linspace(-7-f_s ,-5-f_s ,10)
t210 = np.linspace( -5-f_s , 0-f_s ,10)
t310 = np.linspace( 0-f_s , 5-f_s , 10 )
t410 = np.linspace( 5-f_s , 7-f_s , 10 )
x110=t1*0
x210=t2 +5
x310=-t3+5
x410=t4*0
# x(t)
x0 = np.concatenate(( x110, x210 , x310 , x410 ),axis = 0)
t0=np.concatenate(( t110 , t210  , t310 , t410),axis = 0)
t11 = np.linspace(-7+f_s ,-5+f_s ,10)
t21 = np.linspace( -5+f_s , 0+f_s ,10)
t31 = np.linspace( 0+f_s , 5+f_s , 10 )
t41 = np.linspace( 5+f_s , 7+f_s , 10 )
x11=t1*0
x21=t2 +5
x31=-t3+5
x41=t4*0
# x(t)
x1 = np.concatenate(( x11 , x21 , x31 , x41 ),axis = 0)
t1=np.concatenate(( t11 , t21  , t31 , t41),axis = 0)
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 5, 3
plt.plot(t,x, color ='b')
plt.plot(t1,x1,color ='b', label = 'sampled signal')
plt.plot(t0,x0,color ='b')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.legend(loc='best')
plt.show()
