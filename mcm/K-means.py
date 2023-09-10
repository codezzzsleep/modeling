# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from sklearn.cluster import KMeans
#
# # 格式化原始数据
# data = pd.read_csv("predata.csv").values
#
# data = np.array(data).flatten().reshape(-1, 1)
# n_rows = 251
# n_cols = 201
#
# # 计算坐标
# x_grid, y_grid = np.mgrid[1:(n_cols + 1), 1:(n_rows + 1)]
# xy_coordinates = np.column_stack((x_grid.ravel(), y_grid.ravel()))
#
# # 聚类算法
# kmeans = KMeans(n_clusters=3, random_state=42)
# kmeans.fit(data)
#
# # 聚类结果
# clusters = kmeans.predict(data)
# print(clusters)
# for item in clusters:
#     print(item)
# # 可视化
# plt.figure(figsize=(8, 6))
#
# for i in range(len(data)):
#     plt.scatter(xy_coordinates[i, 0], xy_coordinates[i, 1],
#                 color=["r", "g", "b"][clusters[i]], s=100)
#
# plt.title('K-Means Clustering of the Data')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.gca().invert_yaxis()
# plt.show()
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 准备数据
# 请确保使用您实际的251x201数据替换下面的随机数据
data = pd.read_csv("predata.csv").values

# 确定聚类数量
n_clusters = 3

# 创建KMeans对象并拟合数据
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(data)

# 获取每个点的聚类标签
labels = kmeans.labels_

# 存储中心点（聚类中心）
cluster_centers = kmeans.cluster_centers_

# 将数据降至2维
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(data)
reduced_centers = pca.transform(cluster_centers)

# 绘制栅格
fig, ax = plt.subplots()

# 为每个簇分配一个颜色
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

# 绘制数据点
for i in range(n_clusters):
    cluster_points = reduced_data[labels == i]
    ax.scatter(cluster_points[:, 0], cluster_points[:, 1], c=colors[i % len(colors)], marker='o', label=f'Cluster {i}')

# 绘制中心点
ax.scatter(reduced_centers[:, 0], reduced_centers[:, 1], c='k', marker='x', s=150, label='Centroids')

# 设定图例和坐标轴标签
ax.legend()
ax.set_xlabel('First Principal Component')
ax.set_ylabel('Second Principal Component')

# 展示图形
plt.show()
