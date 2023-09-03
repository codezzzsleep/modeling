import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# from detaile import LinearRegression

# 创建示例数据
data = {'x1': [1, 2, 3, 4, 5],
        'x2': [2, 4, 5, 4, 5],
        'y': [3, 5, 6, 6, 7]}
df = pd.DataFrame(data)

# 提取特征和目标变量
X = df[['x1', 'x2']]
y = df['y']

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X, y)

# 预测
y_pred = model.predict(X)

# 可视化
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['x1'], df['x2'], df['y'], c='blue', marker='o')
ax.plot_trisurf(df['x1'], df['x2'], y_pred, color='red', alpha=0.5)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.title('Multiple Linear Regression')
plt.savefig("logs/multiple.png")
plt.show()
