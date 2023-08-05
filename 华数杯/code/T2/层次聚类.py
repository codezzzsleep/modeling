from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd

df = pd.read_excel("../../dataset/demo_train.xlsx")
type_counts = df['婴儿行为特征'].value_counts()
print(type_counts)
data = df.iloc[:, 1:9].to_numpy()
label = df.iloc[:-20, 9].to_numpy()

# 创建层次聚类模型，指定簇数为3
model = AgglomerativeClustering(n_clusters=3)

# 对数据进行拟合
pred = model.fit_predict(data)

acc_count = 0
for i in range(len(label)):
    if label[i] == pred[i]:
        acc_count += 1

print(acc_count / len(label))
unique_elements, counts = np.unique(pred, return_counts=True)
print(unique_elements, counts)
# 打印每个样本的簇标签
print("样本标签:", pred[-20:])
