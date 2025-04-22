# Data Frames and Basic Data Pre-processing
import pandas as pd

data = pd.read_csv("./dsp2sample.csv")
print(data)

head = data.head(2)
print("The head is ",head)

fillna = data.fillna("Empty")
print(fillna)

dropna = data.dropna()
print(dropna)

filter = data[data["Maths"] > 80]
print(filter )

sort = data.sort_values(by="Science",ascending=False)
print(sort)

grp = data.groupby("Name").mean()
print(grp)
