import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits import mplot3d
ax =plt.axes(projection="3d")
x=np.arange(-5,5,0.1)
y=np.arange(-5,5,0.1)
X,Y=np.meshgrid(x,y)
z=np.sin(X)*np.cos(Y)
ax.plot_surface(X,Y,z,cmap="plasma")
plt.legend()
plt.show()