from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# from detaile import accuracy_score, precision_score, recall_score, f1_score

# 加载鸢尾花数据集
data = load_iris()
X = data.data
y = data.target

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练逻辑回归模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print("准确率：", accuracy)

precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# # 计算精确率
# precision = precision_score(y_test, y_pred)
#
# # 计算召回率
# recall = recall_score(y_test, y_pred)
#
# # 计算F1值
# f1 = f1_score(y_test, y_pred)


print("精确率：", precision)
print("召回率：", recall)
print("F1值：", f1)
