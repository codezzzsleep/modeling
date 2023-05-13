import pandas as pd
import numpy as np
from util.data_process import fix_test_dataset
from util.data_process import fix_train_dataset
from util.data_storage import train_make_dir
from util.data_define import get_features
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
feature_select = 'feature_select'
features = get_features(feature_select)
label_column = ['label']
train_dir = train_make_dir()
pre_path = "../run/train/"+str(train_dir)+"/"+"pre_"+feature_select
pre_pro_path = "../run/train/"+str(train_dir)+"/"+"pre_pro_"+feature_select
train_data, train_target = fix_train_dataset(features, label_column)
train_X, test_X, train_y, test_y = train_test_split(train_data, train_target, test_size=0.3, random_state=5)

clf = tree.DecisionTreeClassifier(criterion='entropy')  # 指明为那个算法
clf = clf.fit(train_X, train_y)

pre = clf.predict(test_X)
pre = pd.Series(pre)
pre.append(test_y)
pre.to_csv(pre_path+".csv")
pre_pro = clf.predict_proba(test_X)
pre_pro = pd.DataFrame(pre_pro)
pre_pro.to_csv(pre_pro_path+".csv")
