from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr

# 准备数据
df = pd.read_excel("../../dataset/demo_train.xlsx")
type_counts = df['婴儿行为特征'].value_counts()
print(type_counts)
X_b = df.iloc[:-20, 1:6].to_numpy()
X_p = df.iloc[:-20, 6:9].to_numpy()
y = df.iloc[:-20, 9].astype(np.int32).to_numpy()
test_b = df.iloc[-20:, 1:6].to_numpy()
test_p = df.iloc[-20:, 6:9].to_numpy()
# 创建PCA对象
k = 1
pca = PCA(n_components=k)
print(X_p.shape)
pca.fit(X_b)
X_b_transformed = pca.transform(X_b)
test_b_transformed = pca.transform(test_b)

pca.fit(X_p)
X_p_transformed = pca.transform(X_p)
test_p_transformed = pca.transform(test_p)

X = np.vstack((X_b_transformed, X_p_transformed))
X = X.reshape(390, 2)
test = np.vstack((test_b_transformed, test_p_transformed))
test = test.reshape(20, 2)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=755)

model = LogisticRegression()

model.fit(X_train, y_train)

pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)

print("进行主成分分析降维后使用逻辑回归模型的精度：", acc)

ans = model.predict(test)
print(ans)
