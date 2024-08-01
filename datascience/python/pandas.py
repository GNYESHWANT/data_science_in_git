#create dataframe
import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print(df)
#Count the number of columns:
count_column = df.shape[1]
print(count_column)
#Count the number of rows:
count_row = df.shape[0]
print(count_row)
#This chapter shows three commonly used functions when working with Data Science: max(), min(), and mean().
Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print (Average_pulse_max)
Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print(Average_pulse_min)
#Extract and Read Data With Pandas
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
print(health_data)
print(health_data.head())#shows top 5 rows
health_data.dropna(axis=0,inplace=True)#remove backspaces
print(health_data)
health_data.dropna(axis=0,inplace=True)#prints data types with in a data set
print(health_data)
#We see that this data set has two different types of data:

#*Float64
#*Object
#We cannot use objects to calculate and perform analysis here. We must convert the type object to float64 (float64 is a number with a decimal in Python).
health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)#changes to float type
print (health_data.info())
#analyse data
print(health_data.describe())