#Import pyplot from Matplotlib and visualize our DataFrame:
import pandas as pd
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('Agg')
df = pd.read_csv('data.csv')
df.plot()
plt.show()
#scatter plot
df = pd.read_csv('data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()
#Three lines to make our compiler able to draw:
df["Duration"].plot(kind = 'hist')
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

