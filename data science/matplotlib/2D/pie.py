import matplotlib.pyplot as plt
x=[25,75]
activity=['dry','wet']
cols=['blue','brown']
plt.pie(x,labels=activity,colors=cols,startangle=90,shadow=True,explode=(0,0),autopct="%.2f")
plt.title("pie chart")
plt.legend()
plt.show()
