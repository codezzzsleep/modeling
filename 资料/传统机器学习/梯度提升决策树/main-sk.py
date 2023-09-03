import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import seaborn as sns

# 加载乳腺癌数据集
data = load_breast_cancer()
X, y = data.data, data.target
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 将数据划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建梯度提升分类器
gb_clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# 使用训练数据对分类器进行拟合
gb_clf.fit(X_train, y_train)

# 使用测试集评估模型
y_pred = gb_clf.predict(X_test)
print("分类报告:\n", classification_report(y_test, y_pred))

# 计算混淆矩阵
cm = confusion_matrix(y_test, y_pred)

# 可视化混淆矩阵
ax = plt.subplot()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)

ax.set_xlabel("预测标签")
ax.set_ylabel("真实标签")
ax.set_title("混淆矩阵")
ax.xaxis.set_ticklabels(["负", "正"])
ax.yaxis.set_ticklabels(["负", "正"])

plt.show()
