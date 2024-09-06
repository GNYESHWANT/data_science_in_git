#Returns True for every row that is a duplicate, otherwise False:
import pandas as pd
df = pd.read_csv('data.csv')
print(df.duplicated())
#To remove duplicates, use the drop_duplicates() method
df.drop_duplicates(inplace = True)
print(df.to_string())
#Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame
