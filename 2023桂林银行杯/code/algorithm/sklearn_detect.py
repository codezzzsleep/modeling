import pandas as pd
import numpy as np
from util.data_process import fix_test_dataset
from util.data_process import fix_train_dataset
from util.data_storage import detect_make_dir
from util.data_define import get_features

from sklearn import preprocessing
from sklearn import tree
feature_select = "impl12"
features = get_features(feature_select)
label_column = ['label']
detect_dir = detect_make_dir()
pre_path = "../run/detect/"+str(detect_dir)+"/"+"pre_"+feature_select
pre_pro_path = "../run/detect/"+str(detect_dir)+"/"+"pre_pro_"+feature_select
train, label = fix_train_dataset(features, label_column)
clf = tree.DecisionTreeClassifier(criterion='entropy')  # 指明为那个算法
clf = clf.fit(train, label)

test = fix_test_dataset(features)
print(np.isnan(test).any())
pre = clf.predict(test)
pre = pd.Series(pre)
# 结果保存
pre.to_csv(pre_path+".csv")
pre_pro = clf.predict_proba(test)
pre_pro = pd.DataFrame(pre_pro)
pre_pro.to_csv(pre_pro_path+".csv")
