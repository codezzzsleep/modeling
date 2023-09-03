import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 加载鸢尾花数据集
iris = load_iris()

# 提取特征和标签
X = iris.data[:, 0]  # 萼片长度作为自变量
y = iris.data[:, 2]  # 花瓣长度作为因变量

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 将输入特征 X 转换为二维数组
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)

# 创建线性回归模型
model = LinearRegression()

# 在训练集上训练模型
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 计算回归的均方误差
mse = mean_squared_error(y_test, y_pred)

# 绘制回归直线和散点图
plt.scatter(X_test, y_test, color='b', label='Actual')
plt.plot(X_test, y_pred, color='r', label='Predicted')
plt.xlabel('Sepal length')
plt.ylabel('Petal length')
plt.title('Linear Regression')
plt.legend()
plt.savefig("logs/simple.png")
plt.show()

# 打印回归的均方误差
print("Mean Squared Error:", mse)
