import sys
sys.path.append(r'E:\studyCode\数模\code\util')
import data_define
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

features = get_features('all')
label_column = ['label']

train_data = pd.read_csv("train.csv")
train = train_data[features]
label = train_data[label_column]
train = pd.get_dummies(train)
tmp = np.isnan(train).any()
fill_column = []
for idx in tmp.index:
    if tmp[idx]:
        fill_column.append(idx)
train[fill_column] = train[fill_column].fillna(train[fill_column].median())

clf = LogisticRegression()
clf = clf.fit(train, label)
########################################################################

test_data = pd.read_csv("test.csv")
print("原始列表")
print(test_data.columns)
test = test_data[features]
test = pd.get_dummies(test)
print("get_dummies后列表")
print(test.columns)
# print(np.isnan(features_test).any())
tmp = np.isnan(test).any()
fill_column = []
for idx in tmp.index:
    if tmp[idx]:
        fill_column.append(idx)
test[fill_column] = test[fill_column].fillna(test[fill_column].median())

print(np.isnan(test).any())

pre = clf.predict(test)
pre_pro = clf.predict_proba(test)
print(pre)
print(pre_pro)
