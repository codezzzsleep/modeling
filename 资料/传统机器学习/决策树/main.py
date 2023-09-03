import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 加载鸢尾花数据
iris = load_iris()
X, y = iris.data, iris.target

# 将数据划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建决策树分类器，并使用训练数据对其进行拟合
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# 绘制决策树
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names.tolist(), filled=True)
plt.savefig("logs/tree.png")
plt.show()
