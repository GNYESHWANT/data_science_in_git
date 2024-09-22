#Return a new Data Frame with no empty cells:
import pandas as pd
df = pd.read_csv('data.csv')
new_df = df.dropna()#he dropna() method returns a new DataFrame, and will not change the original
print(new_df.to_string())
#If you want to change the original DataFrame, use the inplace = True argument
df.dropna(inplace = True)
print(df.to_string())
df.fillna(130, inplace = True)
print(df.to_string())
#Notice in the result: empty cells got the value 130 (in row 18, 22 and 28).
#Calculate the MEAN, and replace any empty values with it:
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
#Calculate the MEDIAN, and replace any empty values with it:
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
#calculate the MODE, and replace any empty values with it:
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
#Cleaning Data of Wrong Format
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())
#removing rows
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())

