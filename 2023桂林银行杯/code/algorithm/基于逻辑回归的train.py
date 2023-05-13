from util.data_define import get_features
from util.data_process import fix_train_dataset
from util.data_process import fix_test_dataset
from util.data_storage import train_make_dir

from sklearn import tree
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

features = get_features('all')
label_column = ['label']

train, label = fix_train_dataset(features, label_column)

clf = tree.DecisionTreeClassifier(criterion='entropy')  # 指明为那个算法
clf = clf.fit(train, label)
########################################################################

# test_data = pd.read_csv("test.csv")
# print("原始列表")
# print(test_data.columns)
# test = test_data[features]
# test = pd.get_dummies(test)
# print("get_dummies后列表")
# print(test.columns)
# # print(np.isnan(features_test).any())
# tmp = np.isnan(test).any()
# fill_column = []
# for idx in tmp.index:
#     if tmp[idx]:
#         fill_column.append(idx)
# test[fill_column] = test[fill_column].fillna(test[fill_column].median())
test = fix_test_dataset(features)
# print(np.isnan(test).any())

pre = clf.predict(test)
pre_pro = clf.predict_proba(test)
print(pre)
print(pre_pro)
