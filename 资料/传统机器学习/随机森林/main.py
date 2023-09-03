import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split

# 加载鸢尾花数据
iris = load_iris()
X, y = iris.data, iris.target

# 将数据划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建随机森林分类器，设置 n_estimators 参数表示森林中树的数量
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)

# 使用训练数据对分类器进行拟合
rf_clf.fit(X_train, y_train)

# 要显示的决策树的数量
num_trees_to_show = 4

fig, axes = plt.subplots(2, 2, figsize=(20, 20))
axes = axes.ravel()  # 将子图数组变成一维数组便于循环
for idx, tree_idx in enumerate(range(num_trees_to_show)):
    single_tree = rf_clf.estimators_[tree_idx]
    plot_tree(single_tree, feature_names=iris.feature_names, class_names=list(iris.target_names), filled=True,
              ax=axes[idx])
    axes[idx].set_title(f"Tree {tree_idx}")
plt.savefig("logs/trees.png")
plt.show()
