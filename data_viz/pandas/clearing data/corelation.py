#Finding Relationships
#A great aspect of the Pandas module is the corr() method.
#The corr() method calculates the relationship between each column in your data set.

import pandas as pd
df = pd.read_csv('data.csv')
print(df.corr())
#         Duration     Pulse  Maxpulse  Calories
#Duration  1.000000 -0.059452 -0.250033  0.344341
#Pulse    -0.059452  1.000000  0.269672  0.481791
#Maxpulse -0.250033  0.269672  1.000000  0.335392
#Calories  0.344341  0.481791  0.335392  1.000000
#perfect correlation=1.0000000
#good correlation=0.922721
#bad correlation=0.009403
