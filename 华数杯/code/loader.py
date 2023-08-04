import pandas as pd

df = pd.read_excel("../dataset/demo.xlsx")
df = df.drop(0)
df = df.iloc[:, :15]
outliers = df[(df['母亲年龄'] < 16) | (df['母亲年龄'] > 75)]
print(outliers)
