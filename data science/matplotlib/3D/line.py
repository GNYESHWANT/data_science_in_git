import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining all 3 axis
x=np.arange(0,50,0.1)
y=np.arange(0,50,0.1)
z=x*y
# plotting
ax.plot(x, y, z, color='blue',marker="*",alpha=0.1)
ax.set_title('3D line plot geeks for geeks')
plt.show()
