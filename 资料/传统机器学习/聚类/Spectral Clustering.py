import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import SpectralClustering

# 生成模拟数据集
data, labels = datasets.make_blobs(n_samples=1000, centers=4, random_state=42)

# 可视化数据
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap="viridis")
plt.show()
spectral_clustering = SpectralClustering(n_clusters=4, affinity="nearest_neighbors")
spectral_labels = spectral_clustering.fit_predict(data)

# 可视化结果
plt.scatter(data[:, 0], data[:, 1], c=spectral_labels, cmap="viridis")
plt.show()
