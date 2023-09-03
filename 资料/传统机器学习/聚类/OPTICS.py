import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import OPTICS

# 生成模拟数据集
data, labels = datasets.make_blobs(n_samples=1000, centers=4, random_state=42)

# 可视化数据
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap="viridis")
plt.show()
optics = OPTICS(min_samples=5, max_eps=1.5)
optics_labels = optics.fit_predict(data)

# 可视化结果
plt.scatter(data[:, 0], data[:, 1], c=optics_labels, cmap="viridis")
plt.show()
