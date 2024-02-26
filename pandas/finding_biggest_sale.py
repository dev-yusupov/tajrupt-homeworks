import pandas as pd

df = pd.read_csv('vgsales.csv')

df = df.dropna(axis=0)

dict_years = {}

for index, row in df.iterrows():
    year = row['Year']
    sales = row['Global_Sales']
    
    if year in dict_years:
        dict_years[year] += float(sales)

    else:
        dict_years[year] = float(sales)

max_sales = max(dict_years.values())

years_with_max_sales = [year for year, sales in dict_years.items() if sales == max_sales]

print("Year(s) with the greatest global sales:", years_with_max_sales)
print("Greatest global sales:", max_sales)
