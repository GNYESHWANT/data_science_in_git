#Create a simple Pandas Series from a list:
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)

print(myvar)
#Create Labels
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
#Key/Value Objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
#note the keys of dictionary becomes labels
#Create a DataFrame from two Series:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
print(df.loc[0])#Locate Row
#use a list of indexes:
print(df.loc[[0, 1]])
#named index
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
#refer to the named index:
print(df.loc["day2"])
#Load Files Into a DataFrame
# 1 CSV
df = pd.read_csv('data.csv')
print(df) 
print(df.to_string()) #used to_string() to print the entire DataFrame
print(pd.options.display.max_rows)#Check the number of maximum returned rows

#2.JSON
df = pd.read_json('data.json')
print(df.to_string()) 
#Load a Python Dictionary into a DataFrame:
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
print(df) 
#Analyzing DataFrames
df = pd.read_csv('data.csv')
print(df.head(10))#the head() method will return the top 5 rows.
print(df.tail())#the tail() method returns the headers and a specified number of rows, starting from the bottom
