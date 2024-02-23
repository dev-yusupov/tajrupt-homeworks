import pandas

df = pandas.read_csv('vgsales.csv')

mn = df['Global_Sales'].min()
mx = df['Global_Sales'].max()

df['Sales_somoni'] = df['Global_Sales'] * 11 * 1000000

ps4_count = 0

for i in range(len(df['Platform'])):
    if df['Platform'][i] == 'PS4':
        ps4_count += 1


print(ps4_count)