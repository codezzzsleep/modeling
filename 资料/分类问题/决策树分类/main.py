import matplotlib.pyplot as plt
from sklearn import datasets,  tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import classification_report

# 加载示例数据集（以鸢尾花数据集为例）
iris = datasets.load_iris()
X = iris.data  # 特征
y = iris.target  # 目标变量

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# 创建决策树分类器对象
clf = DecisionTreeClassifier()

# 在训练集上训练决策树模型
clf.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = clf.predict(X_test)

# 生成分类报告
report = classification_report(y_test, y_pred)
print("分类报告:")
print(report)

# 可视化决策树
plt.figure(figsize=(10, 7))
tree.plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()

# 保存模型
import joblib
joblib.dump(clf, 'decision_tree_model.pkl')
