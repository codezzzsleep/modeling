import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# from detaile import LinearRegression

# 创建示例数据
data = {'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 5, 4, 5]}
df = pd.DataFrame(data)

# 提取特征和目标变量
X = df[['x']]
y = df['y']

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X, y)

# 预测
y_pred = model.predict(X)

# 可视化
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.savefig("logs/simple.png")
plt.show()
