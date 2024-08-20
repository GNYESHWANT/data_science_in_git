import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.xlabel('x')
plt.ylabel('y')
plt.title("histagraph")
plt.legend()
plt.show()
