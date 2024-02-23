import pandas

df = pandas.read_csv('vgsales.csv')

df = df.dropna(axis=0)
dict_years = {}

years = list(df['Year'])
sales = list(df['Global_Sales'])


for year in years:
    inx = years.index(year)
    if year in dict_years.keys():
        dict_years[year] += sales[inx]

    else:
        dict_years[year] = sales[inx]


print(dict_years)
