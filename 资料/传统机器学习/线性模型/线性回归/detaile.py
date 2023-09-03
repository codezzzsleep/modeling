import numpy as np
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
