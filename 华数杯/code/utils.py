import pandas as pd

'''
对训练用的数据集使用均值进行填充
'''
df = pd.read_excel("../dataset/demo_train.xlsx")
mean_value = df['妊娠时间（周数）'].mean()

# 对特定列进行均值填充
df['妊娠时间（周数）'].fillna(mean_value, inplace=True)
df.to_excel('../dataset/demo_train.xlsx', index=False)

na_count_per_column = df.isna().sum()

print(na_count_per_column)