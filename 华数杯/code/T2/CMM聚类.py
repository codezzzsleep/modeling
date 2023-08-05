from sklearn.mixture import GaussianMixture
import numpy as np
import pandas as pd

df = pd.read_excel("../../dataset/demo_train.xlsx")
type_counts = df['婴儿行为特征'].value_counts()
print(type_counts)
data = df.iloc[:, 1:9].to_numpy()
label = df.iloc[:-20, 9].to_numpy()

# 创建GMM聚类模型，指定组件数（簇数）
n_components = 3
model = GaussianMixture(n_components=n_components)

# 对数据进行拟合
model.fit(data)

# 获取每个样本所属的簇标签
pred = model.predict(data)
acc_count = 0
for i in range(len(label)):
    if label[i] == pred[i]:
        acc_count += 1

print(acc_count / len(label))
# 获取每个簇的均值和协方差矩阵
means = model.means_
covariances = model.covariances_
unique_elements, counts = np.unique(pred, return_counts=True)
print(unique_elements, counts)
print("样本标签:", pred)
print("簇均值:", means)
print("簇协方差矩阵:", covariances)
