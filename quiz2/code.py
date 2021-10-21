import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

fig, ax = plt.subplots(figsize = (6,6))

ax.set_xlim([-3,3])
ax.set_ylim([-3,3])

pole, = plt.plot(-1,0, 'rx',label = 'Poles')
zero, = plt.plot(1,0, 'ro',label = 'Zeros')

legend = plt.legend(handles =[pole,zero], loc = 'lower right')
fig.gca().add_artist(legend)

circle = plt.Circle([0,0],1,color = 'w')
fig.gca().add_artist(circle)

circle = plt.Circle([0,0],1,edgecolor = 'black',fill = 0,linestyle = '--')
fig.gca().add_artist(circle)

patches = mpatches.Patch(color="blue", label="ROC")
dotted_line = mlines.Line2D([],[],color = 'black',label='Unit circle')
dotted_line.set_linestyle('--')
plt.legend(handles=[patches,dotted_line], loc = 'upper right')
ax.set_facecolor('xkcd:blue')
plt.title("Pole-Zero Plot with ROC")
plt.grid()
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
