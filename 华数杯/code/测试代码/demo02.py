import pandas as pd
import numpy as np

df = pd.read_csv("../../dataset/睡眠质量分类预测.csv")

df = df['预测结果_Y'].astype(np.int32)
for i in df:
    print(i, end=' ')
