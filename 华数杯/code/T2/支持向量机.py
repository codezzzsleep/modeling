from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np

df = pd.read_excel("../../dataset/demo_train.xlsx")
type_counts = df['婴儿行为特征'].value_counts()
print(type_counts)
X = df.iloc[:-20, 1:9].to_numpy()
y = df.iloc[:-20, 9].astype(np.int32).to_numpy()
test = df.iloc[-20:, 1:9].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=755)

svm_classifier = SVC(kernel='linear')  # 使用线性核函数

svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("支持向量机准确率：", accuracy)

ans = svm_classifier.predict(test)
print(ans)
