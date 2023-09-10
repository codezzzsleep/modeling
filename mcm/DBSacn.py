import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN

# 你的海底深度数据，这里用一个示例数据代替
depth_data = pd.read_csv("predata.csv").values

# 创建一个DBSCAN模型
dbscan = DBSCAN(eps=0.01, min_samples=3)  # 根据数据的密度分布调整eps和min_samples参数

# 拟合模型并获取每个数据点的所属簇标签
cluster_labels = dbscan.fit_predict(depth_data.reshape(-1, 1))  # 将数据转换为一维数组
print(cluster_labels)
print(len(cluster_labels))
# 创建热图，根据聚类结果着色
plt.figure(figsize=(8, 6))
plt.imshow(cluster_labels.reshape(depth_data.shape), extent=(0, 1, 0, 1), origin='lower', cmap='viridis')
plt.colorbar(label='Cluster Label')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('DBSCAN Clustering Result')
plt.show()
