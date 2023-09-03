# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from detaile import LinearDiscriminantAnalysis

# 加载数据集
data = load_iris()
X = data.data
y = data.target

# 拆分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练LDA模型
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

# 预测测试集
y_pred = lda.predict(X_test)

# 打印分类报告
report = classification_report(y_test, y_pred)
print("Classification Report:")
print(report)
