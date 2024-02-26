import pandas as pd

df = pd.read_csv('vgsales.csv')

df.dropna(axis=0)

sale_dict = {}

for index, row in df.iterrows():
    platform = row['Platform']
    sales = row['Global_Sales']

    if platform in sale_dict:
        sale_dict[platform] += float(sales)
    
    else:
        sale_dict[platform] = float(sales)


max_sale = max(sale_dict.values())

popular_platform = [platform for platform, price in sale_dict.items() if price==max_sale]

print(popular_platform)
print(max_sale)