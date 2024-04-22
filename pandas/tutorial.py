import pandas as pd

df = pd.read_csv('vgsales.csv')

print(df.head(10)) # Used to see the first n rows of data from dataset. head(n)
print(df.tail(10)) # Used to see the last n rows of data from dataset. tail(n)

# df['Name of column'] is used to see the data of columns with name "Name of column"

platforms = df['Platform'] 
print(platforms)

