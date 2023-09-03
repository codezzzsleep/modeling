import matplotlib.pyplot as plt
import numpy as np

# from sklearn.linear_model import LinearRegression
from detaile import LinearRegression

# 准备数据
X = np.array([[1], [2], [3], [4], [5]])  # 输入特征
y = np.array([2, 4, 6, 8, 10])  # 输出目标

# 创建线性回归模型对象
model = LinearRegression()

# 训练模型
model.fit(X, y)

# 生成预测结果
X_pred = np.linspace(0, 6, 100).reshape(-1, 1)
y_pred = model.predict(X_pred)

# 绘制数据点和拟合曲线
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_pred, y_pred, color='red', label='Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.savefig("logs/linear.png")
plt.show()
