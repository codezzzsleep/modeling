import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("../dataset/demo.xlsx")

type_map = {'中等型': 0, '安静型': 1, '矛盾型': 2}
df['婴儿行为特征'] = df['婴儿行为特征'].replace(type_map)
df['整晚睡眠时间（时：分：秒）'] = df['整晚睡眠时间（时：分：秒）'].astype(str).str.strip()
df['整晚睡眠时间（时：分：秒）'] = pd.to_datetime(df['整晚睡眠时间（时：分：秒）'], format='%H:%M:%S', errors='coerce').dt.time
df['整晚睡眠时间（时：分：秒）'] = df['整晚睡眠时间（时：分：秒）'].apply(lambda x: x.hour + x.minute / 60 + x.second / 3600)
df.to_excel('../dataset/demo_train.xlsx', index=False)
del df['婴儿性别']
del df['婴儿年龄（月）']
correlation_matrix = df.corr()
plt.rcParams['font.sans-serif'] = ['SimSun']

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('相关性热力图')
plt.savefig("png/相关性分析热力图.png")
plt.show()
