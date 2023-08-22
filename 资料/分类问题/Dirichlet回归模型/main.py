import numpy as np
from dirichlet import Dirichlet
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# 生成示例数据
X, y = make_classification(n_samples=100, n_features=5, n_informative=3, n_classes=4, random_state=42)

# 将类别标签转换为比例向量
y = np.eye(np.unique(y).shape[0])[y]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建Dirichlet回归模型对象
model = Dirichlet()

# 拟合模型
model.fit(X_train, y_train)

# 预测测试集
y_pred = model.predict(X_test)

# 计算准确率
accuracy = np.mean(np.argmax(y_pred, axis=1) == np.argmax(y_test, axis=1))
print("Accuracy:", accuracy)
