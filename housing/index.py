from typing import List

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv("housing.csv")
pd.set_option("display.max_columns", None)
# pd.set_option("display.max_row", None)

def min_max_normalization(data: pd.DataFrame, range_: str) -> pd.DataFrame:
    normalized_data = pd.DataFrame()
    for column in data.columns:
        min_val = data[column].min()
        max_val = data[column].max()

        if range_ == "1-1":
            normalized_data[column] = 2 * (data[column] - min_val) / (max_val - min_val) - 1
        elif range_ == "0-1":
            normalized_data[column] = (data[column] - min_val) / (max_val - min_val)

    return normalized_data

columns = ["housing_median_age", "total_rooms", "total_bedrooms", "population", "households", "median_income", "median_house_value"]

# print(dataset['median_house_value'].mean())
# print(dataset['median_house_value'].max())
# print(dataset['median_house_value'].min())
# print(dataset['median_house_value'].median())

dataset = dataset.dropna(axis=0)

Y = pd.DataFrame()
Y['price'] = dataset["median_house_value"]

X = pd.DataFrame()
X['age'] = dataset["housing_median_age"]
X["rooms"] = dataset["total_rooms"]
X["bedrooms"] = dataset["total_bedrooms"]
X["population"] = dataset["population"]
X["families"] = dataset["households"]
X["median_income"] = dataset["median_income"]

X_mas = min_max_normalization(X, range_="0-1")
Y_mas = min_max_normalization(Y, range_="0-1")

X = pd.DataFrame(X_mas, columns=X.columns)
Y = pd.DataFrame(Y_mas, columns=Y.columns)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

mse = mean_squared_error(Y_test, Y_pred)

print(mse**0.5)