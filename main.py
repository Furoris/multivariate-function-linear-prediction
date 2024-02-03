import pandas as pd
from sklearn import linear_model
import math
from input_validator import InputValidator


# Get and validate input
validator = InputValidator()
area = validator.get_input('AREA')
bedrooms = validator.get_input('BEDROOMS')
age = validator.get_input('AGE')

# Read data frame and fill missing data
df = pd.read_csv('homeprices.csv')
df.bedrooms = df.bedrooms.fillna(math.floor(df.bedrooms.median()))

# Fitting linear model
reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'age']].values, df.price)

# Prediction of price
prediction = reg.predict([[area, bedrooms, age]])
print("Predicted price $" + str(round(prediction[0], 2)))

