from util.data_define import get_features
from util.data_process import fix_train_dataset
from util.data_process import fix_test_dataset
from util.data_storage import detect_make_dir
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

test = fix_test_dataset(features)

pre = clf.predict(test)
pre_pro = clf.predict_proba(test)
print(pre)
print(pre_pro)
