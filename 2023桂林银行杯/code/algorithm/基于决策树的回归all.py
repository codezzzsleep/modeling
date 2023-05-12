# import sys
from util.data_define import get_features
# sys.path.append(r'E:\studyCode\数模\code\util')
# from data_define import get_features
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import tree

features = get_features('impl15')
label_column = ['label']

train_data = pd.read_csv("../data/train.csv")
train = train_data[features]
label = train_data[label_column]
train = pd.get_dummies(train)
tmp = np.isnan(train).any()
fill_column = []
for idx in tmp.index:
    if tmp[idx]:
        fill_column.append(idx)
train[fill_column] = train[fill_column].fillna(train[fill_column].median())

clf = tree.DecisionTreeClassifier(criterion='entropy')  # 指明为那个算法
clf = clf.fit(train, label)
########################################################################

test_data = pd.read_csv("../data/test.csv")
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
pre = pd.Series(pre)
pre.to_csv("../run/detect/4/pre_impl15.csv")
pre_pro = clf.predict_proba(test)
pre_pro = pd.DataFrame(pre_pro)
pre_pro.to_csv("../run/detect/4/pre_pro_impl15.csv")
