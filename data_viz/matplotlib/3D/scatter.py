import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining all 3 axis
x=np.random.randint(0,100,(500,))
y=np.random.randint(0,100,(500,))
z=np.random.randint(0,100,(500,))
# plotting
ax.scatter(x, y, z, color='green',marker="*",alpha=0.1)
ax.set_title('3D line plot geeks for geeks')
plt.show()
