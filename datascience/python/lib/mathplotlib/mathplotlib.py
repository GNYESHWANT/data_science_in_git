#line plot
import matplotlib.pyplot as plt
x=[123]
y=[574]
x2=[1,2,3]
y2=[10,14,12]
plt.plot(x,y,label="line1")
plt.plot(x2,y2,label="line2")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('LINE GRAPH')
plt.legend()
plt.show()
#bar chart
plt.bar(x2,y2)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('LINE GRAPH')
plt.legend()
plt.show()
#pie chart
import matplotlib.pyplot as plt
sizes=[89,80,90,100,75]
labels=["tamil","English","maths","science","social"]
plt.pie(sizes,label=labels,autopct="%2f")
plt.show()
#histogram
plt.hist(x2,y2)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('LINE GRAPH')
plt.legend()
plt.show()
#pareoto chart
import pandas as pd

#create DataFrame
df = pd.DataFrame({'count': [97, 140, 58, 6, 17, 32]})
df.index = ['B', 'A', 'C', 'F', 'E', 'D']

#sort DataFrame by count descending
df = df.sort_values(by='count', ascending=False)

#add column to display cumulative percentage
df['cumperc'] = df['count'].cumsum()/df['count'].sum()*100

#view DataFrame
df
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

#define aesthetics for plot
color1 = 'steelblue'
color2 = 'red'
line_size = 4

#create basic bar plot
fig, ax = plt.subplots()
ax.bar(df.index, df['count'], color=color1)

#add cumulative percentage line to plot
ax2 = ax.twinx()
ax2.plot(df.index, df['cumperc'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

#specify axis colors
ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)

#display Pareto chart
plt.show