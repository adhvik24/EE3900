import numpy as np
import matplotlib.pyplot as plt
t1 = np.linspace(-7 ,-5 ,10)
t2 = np.linspace( -5 , 0 ,10)
t3 = np.linspace( 0 , 5 , 10 )
t4 = np.linspace( 5 , 7 , 10 )
x1=t1*0
x2=t2 +5
x3=-t3+5
x4=t4*0
# x(t)
x = np.concatenate(( x1 , x2 , x3 , x4 ),axis = 0)
t=np.concatenate(( t1 , t2  , t3 , t4),axis = 0)
plt.plot(t,x,label = 'signal x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.legend(loc='best')
plt.show()
