import pandas as pd

df = pd.read_csv("vgsales.csv")

count_console = df['Platform'].value_counts()

count_console_dict = {}


for count in count_console.items():
    count_console_dict[count[0]] = count[1]


max_sale = max(count_console_dict.values())
max_console = [console for console, count in count_console_dict.items() if count == max_sale]

print(max_console[0], max_sale)