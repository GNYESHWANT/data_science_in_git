#Install Seaborn.
#If you have Python and PIP already installed on a system, install it using this command:

#C:\Users\Your Name>pip install seaborn
#Plotting a Distplot
#Example 
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()
#Plotting a Distplot Without the Histogram
#Example
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()