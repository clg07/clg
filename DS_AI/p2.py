import pandas as pd

data = pd.read_csv("./dsp2sample.csv")
print(data)

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