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
unique, counts = np.unique(pred, return_counts=True)

# 根据频率排序元素
sorted_indices = np.argsort(-counts)
sorted_elements = unique[sorted_indices]

# 创建替换字典
replace_dict = {sorted_elements[i]: i for i in range(len(sorted_elements))}

# 替换数组中的元素
pred_replaced = np.vectorize(replace_dict.get)(pred)
unique, counts = np.unique(pred_replaced, return_counts=True)

acc_count = 0
for i in range(len(label)):
    if label[i] == pred_replaced[i]:
        acc_count += 1

print(acc_count / len(label))
print(unique, counts)
# 获取簇的中心点
centroids = model.cluster_centers_
# 打印每个样本的簇标签和簇中心点
print("样本标签:", pred_replaced[-20:])
print("簇中心点:", centroids)
