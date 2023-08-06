from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr

# 准备数据
df = pd.read_excel("../../dataset/demo_train.xlsx")
df = df.drop(df.tail(20).index)

X_b = df.iloc[:, 1:6].to_numpy()
X_p = df.iloc[:, 6:9].to_numpy()
X_s = df.iloc[:, 12:15].to_numpy()
test = df.iloc[:, 9].to_numpy()
print("X_b\n", df.iloc[:, 1:6].isna().sum())
print("X_p\n", df.iloc[:, 6:9].isna().sum())
print("X_s\n", df.iloc[:, 12:15].isna().sum())
print("test\n", df.iloc[:, 9].isna().sum())
# 创建PCA对象
k = 1
pca = PCA(n_components=k)

pca.fit(X_b)
X_b_transformed = pca.transform(X_b)

pca.fit(X_p)
X_p_transformed = pca.transform(X_p)

pca.fit(X_s)
X_s_transformed = pca.transform(X_s)

X = np.vstack((X_b_transformed, X_p_transformed, X_s_transformed))
X = X.reshape(390, 3)
X = pd.DataFrame(X, columns=['母亲身体特征PCA', '母亲心理特征PCA', '婴儿睡眠质量PCA'])
y = pd.DataFrame(test, columns=['婴儿行为特征'])

Z = pd.concat([X, y], axis=1)
corr = Z.corr()
# Z.to_excel("../../dataset/主成分分析数据.xlsx")
print(corr)
F = pd.concat([df.iloc[:, 1:6], df.iloc[:, 6:9], df.iloc[:, 9], df.iloc[:, 12:15], X], axis=1)
print(F.corr())
# F.to_excel("../../dataset/原始数据+主成分分析数据.xlsx")
