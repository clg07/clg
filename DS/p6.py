# Import required libraries
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


housing = fetch_california_housing()
housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
print(housing_df)
# Add target (PRICE column)
housing_df['PRICE'] = housing.target


print("\n------ Simple Linear Regression ------")
X = housing_df[['AveRooms']]  # One feature
y = housing_df['PRICE']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

simple_model = LinearRegression()
simple_model.fit(X_train, y_train)

y_pred_simple = simple_model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred_simple))
print("R-squared:", r2_score(y_test, y_pred_simple))
print("Intercept:", simple_model.intercept_)
print("Coefficient:", simple_model.coef_)

 
print("\n------ Multiple Linear Regression ------")
X_multi = housing_df.drop('PRICE', axis=1)  # All features
y_multi = housing_df['PRICE']

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

multi_model = LinearRegression()
multi_model.fit(X_train_m, y_train_m)

y_pred_multi = multi_model.predict(X_test_m)

print("Mean Squared Error:", mean_squared_error(y_test_m, y_pred_multi))
print("R-squared:", r2_score(y_test_m, y_pred_multi))
print("Intercept:", multi_model.intercept_)
print("Coefficients:\n", pd.Series(multi_model.coef_, index=X_multi.columns))
