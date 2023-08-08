from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np
import eli5

df = pd.read_excel("../../dataset/demo_train.xlsx")
type_counts = df['婴儿行为特征'].value_counts()
print(type_counts)
X = df.iloc[:-20, 1:9].to_numpy()
y = df.iloc[:-20, 9].astype(np.int32).to_numpy()
test = df.iloc[-20:, 1:9].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=755)

svm_classifier = SVC(kernel='linear')

svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("支持向量机准确率：", accuracy)

ans = svm_classifier.predict(test)
print(ans)

weights = svm_classifier.coef_
features = df.iloc[:, 1:9].columns.tolist()
for feature, weight in zip(features, weights[0]):
    print(f"{feature}, : {weight}")

# # 获取支持向量
# support_vectors = svm_classifier.support_vectors_
# # 获取支持向量的拉格朗日乘子
# dual_coefs = svm_classifier.dual_coef_
# # 获取截距
# intercept = svm_classifier.intercept_
# # 打印支持向量、拉格朗日乘子和截距
# print("支持向量:", support_vectors)
# print("拉格朗日乘子:", dual_coefs)
# print("截距:", intercept)
decision_values = svm_classifier.decision_function(X)
print(type(decision_values[237]))
# 打印决策函数的值
print(decision_values.shape)
print(decision_values[237])
print(y[237])
print(X_test.shape)
tagert = X[237].reshape(1, 8)
print(tagert.shape)
print()
print(svm_classifier.predict(tagert))
print(y_pred)
