import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 准备数据
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'y': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
})

X = data[['X']].values
y = data['y'].values

# 创建对数几率回归模型对象
model = LogisticRegression()

# 训练模型
model.fit(X, y)

# 绘制决策边界和样本点
plt.scatter(X, y, color='blue', label='Sample Points')

# 生成决策边界的X值
X_boundary = np.linspace(np.min(X), np.max(X), 100).reshape(-1, 1)

# 预测决策边界的y值
y_boundary = model.predict_proba(X_boundary)[:, 1]

# 绘制决策边界
plt.plot(X_boundary, y_boundary, color='red', label='Decision Boundary')

# 设置图例和标题
plt.legend()
plt.title('Logistic Regression - Decision Boundary')
plt.savefig("logs/logistic.png")
# 显示图形
plt.show()
