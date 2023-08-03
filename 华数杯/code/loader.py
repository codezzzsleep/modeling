import pandas as pd

df = pd.read_excel("../dataset/demo.xlsx")
df = df.iloc[:, :15]
print(df)
