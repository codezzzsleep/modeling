from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree

# 加载数据集
df = pd.read_excel("../../dataset/demo_train.xlsx")
type_counts = df['婴儿行为特征'].value_counts()
print(type_counts)
X = df.iloc[:-20, 1:9].to_numpy()
y = df.iloc[:-20, 9].astype(np.int32).to_numpy()
test = df.iloc[-20:, 1:9].to_numpy()

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=755)
print(X_train.shape)
print(X_train)

# 创建随机森林分类器
clf = RandomForestClassifier(n_estimators=128, random_state=42)

# 在训练集上训练模型
clf.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = clf.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print("随机森林准确率:", accuracy)

ans = clf.predict(test)
# ans = clf.predict()
print(X[237].reshape(1, 8).shape)
print(y[237])
print(ans)
tree.plot_tree(clf.estimators_[0])
plt.show()
feature_importances = clf.feature_importances_
feature_names = df.columns[1:9]
# 打印特征重要性
for feature, importance in zip(feature_names, feature_importances):
    print(f"{feature}: {importance}")

import treeinterpreter as ti
interpreter = ti.treeinterpreter.TreeInterpreter(clf)
importances = interpreter.feature_importance()
from sklearn.tree import export_graphviz
export_graphviz(clf.estimators_[0], 'tree.dot', feature_names=feature_names)
