from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

df = pd.read_excel("../../dataset/demo_train.xlsx")
type_counts = df['婴儿行为特征'].value_counts()
print(type_counts)
data = df.iloc[:, 1:9].to_numpy()
label = df.iloc[:-20, 9].to_numpy()

# 创建K-means聚类模型，指定簇数（K）
k = 3
model = KMeans(n_clusters=k)

# 对数据进行拟合
model.fit(data)

# 获取每个样本所属的簇标签
pred = model.labels_
acc_count = 0
for i in range(len(label)):
    if label[i] == pred[i]:
        acc_count += 1

print(acc_count / len(label))
# 获取簇的中心点
centroids = model.cluster_centers_
unique_elements, counts = np.unique(pred, return_counts=True)
print(unique_elements, counts)
# 打印每个样本的簇标签和簇中心点
print("样本标签:", pred[-20:])
print("簇中心点:", centroids)
