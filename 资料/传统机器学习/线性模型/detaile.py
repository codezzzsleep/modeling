import numpy as np
import pandas as pd
from numpy.linalg import lstsq


class LinearRegression:
    def __init__(self):
        self.coefficients = None

    def fit(self, X, y):
        # 添加常数项列
        X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)

        # 使用最小二乘法求解系数
        self.coefficients = lstsq(X, y, rcond=None)[0]

    def predict(self, X):
        # 添加常数项列
        X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)

        # 预测
        y_pred = np.dot(X, self.coefficients)
        return y_pred


# 准备数据
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
})

X = data[['X']].values
y = data['y'].values

# 创建线性回归模型对象
model = LinearRegression()

# 训练模型
model.fit(X, y)

# 使用模型进行预测
X_pred = np.array([[6], [7], [8]])
y_pred = model.predict(X_pred)

print("预测结果：", y_pred)
