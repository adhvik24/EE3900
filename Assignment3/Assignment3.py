import numpy as np
import math
from matplotlib import pyplot as plt

#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Input parameters
C1 = np.array(([0,0]))
C2 = np.array(([4,-3]))
A = np.array(([8,1.5]))
B = np.array(([-4, -4.5]))
r = np.sqrt(5)

#Plotting the circles
x_circ1= circ_gen(C1,r)
plt.plot(x_circ1[0,:],x_circ1[1,:],label = '$||x||^2 = 5$')
x_circ2= circ_gen(C2,r)
plt.plot(x_circ2[0,:],x_circ2[1,:],label = '$  x^Tx-(-8 , 6)x+20 = 0$')



#Plotting the lines

x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$x-2y=5 $')


A = np.array(([0,0]))
B = np.array(([4,-3]))
D = np.array(([1,-2]))
E = np.array(([3,-1]))

#Labeling the coordinates
coords = np.vstack((A,B,D,E)).T
plt.scatter(coords[0,:], coords[1,:])
vert_labels = ['A','B','D','E']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, (coords[0,i], coords[1,i]), textcoords="offset points", xytext=(0,10),ha='center')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right',fontsize=9)
plt.grid()
plt.axis('equal')
