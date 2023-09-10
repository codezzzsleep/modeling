import numpy as np

# 定义X和Y的数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# 生成网格
X, Y = np.meshgrid(x, y)

# 计算对应的Z值
Z = np.sin(np.sqrt(X**2 + Y**2))
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# 创建一个三维坐标系
fig = plt.figure()
ax = plt.axes(projection='3d')

# 绘制三维曲面图
ax.plot_surface(X, Y, Z, cmap='viridis')

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()
