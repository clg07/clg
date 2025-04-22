# Feature Scaling and Dummification
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

data = pd.read_csv("./dsp3sample.csv")
print(data)

# Min-Max Scaling
minmax = MinMaxScaler()
data[['Alcohol', 'Malic Acid']] = minmax.fit_transform(data[['Alcohol', 'Malic Acid']])
print(data)

# Standard Scaling
standard = StandardScaler()
data[['Alcohol', 'Malic Acid']] = standard.fit_transform(data[['Alcohol', 'Malic Acid']])
print(data)

# Label Encoding
le = LabelEncoder()
data['Label_Code'] = le.fit_transform(data['classlabel'])
print(data)
