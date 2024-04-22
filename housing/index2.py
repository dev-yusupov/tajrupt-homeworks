import pandas as pd

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

dataset = pd.read_csv("housing.csv")
pd.set_option("display.max_columns", None)
# pd.set_option("display.max_row", None)

columns = ['housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_house_value']

dataset = dataset.dropna(axis=0)

# Create Y data frame
Y = pd.DataFrame() # Create a new data frame
Y = dataset[['median_house_value']] # Put house price into data frame

# Create X data frame
X = pd.DataFrame() # Create a new data frame
# Include columns into X data frame from dataset
X['age'] = dataset[['housing_median_age']]
X['rooms'] = dataset[['total_rooms']]
X['bedrooms'] = dataset[['total_bedrooms']]
X['population'] = dataset[['population']]

# Scaling values of X and Y data frames
scaler = MinMaxScaler()
X_standardized = scaler.fit_transform(X)
Y_standardized = scaler.fit_transform(Y)

X = pd.DataFrame(X_standardized, columns=X.columns)
Y = pd.DataFrame(Y_standardized, columns=Y.columns)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

mae = mean_absolute_error(Y_pred, Y_test)
mse = mean_squared_error(Y_pred, Y_test)

print(mae)
print(mse)