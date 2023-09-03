import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 加载鸢尾花数据集
iris = load_iris()

# 提取特征和标签
X = iris.data[:, :2]  # 只使用前两个特征以便绘制图形
y = iris.target

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建逻辑回归模型
model = LogisticRegression()

# 在训练集上训练模型
model.fit(X_train, y_train)

# 绘制决策边界
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
plt.contourf(xx, yy, Z, alpha=0.8)

# 绘制训练集和测试集的散点图
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, marker='o', label='train')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker='s', label='test')

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Logistic Regression')
plt.legend()
plt.savefig("logs/logistic.png")
plt.show()

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 打印准确率、召回率、F1 分数等指标
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)
