import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 生成随机的三维数据
np.random.seed(0)
n = 100
x1 = np.random.randn(n)
y1 = np.random.randn(n)
z1 = np.random.randn(n)

x2 = np.random.randn(n)
y2 = np.random.randn(n)
z2 = np.random.randn(n)

# 创建三维散点图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制第一组数据的散点图，颜色为红色
ax.scatter(x1, y1, z1, c='r', label='Data 1')

# 绘制第二组数据的散点图，颜色为蓝色
ax.scatter(x2, y2, z2, c='b', label='Data 2')

# 设置坐标轴标签和图例
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# 显示图形
plt.show()
