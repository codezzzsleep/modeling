x = 15
y = 22
z = 18
k1 = 2612 / 3
b1 = 200
k2 = 695
b2 = 500
k3 = 2240
b3 = 300
import pandas as pd

df = pd.DataFrame(columns=['CBTS', 'EPDS', 'HADS', 'Cost'])

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            tmp = []
            tmp.append(x - i)
            tmp.append(y - j)
            tmp.append(z - k)
            tmp.append(i * k1 + b1 + j * k2 + b2 + k * k3 + b3)
            df.loc[len(df.index)] = tmp
            # print("x = ", x - i, " y = ", y - j, " z = ", z - k)
print(df)
df.to_excel("../../dataset/CEH-Cost.xlsx")