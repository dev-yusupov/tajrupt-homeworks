import pandas as pd

df = pd.read_csv('vgsales.csv')

stats = df.describe()

print(stats)