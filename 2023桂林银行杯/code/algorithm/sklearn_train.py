from util.data_process import fix_train_dataset, get_score
from util.data_storage import train_make_dir
from util.data_define import get_features
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd

feature_select = 'impl15'
features = get_features(feature_select)
label_column = ['label']
train_dir = train_make_dir()
path = "../run/train/" + str(train_dir) + "/"
pre_path = "../run/train/" + str(train_dir) + "/" + "pre_" + feature_select
pre_pro_path = "../run/train/" + str(train_dir) + "/" + "pre_pro_" + feature_select
train_data, train_target = fix_train_dataset(features, label_column)
train_X, test_X, train_y, test_y = train_test_split(train_data, train_target, test_size=0.5)

clf = tree.DecisionTreeClassifier(criterion='entropy')  # 指明为那个算法
clf = clf.fit(train_X, train_y)

pre = clf.predict(test_X)
pre = pd.Series(pre)
pre.to_csv(pre_path + ".csv")

pre_pro = clf.predict_proba(test_X)
pre_pro = pd.DataFrame(pre_pro)
pre_pro.to_csv(pre_pro_path + ".csv")

acc = accuracy_score(test_y, pre)
f1 = f1_score(test_y, pre)
print(acc)
print(f1)
print("score = " + get_score(acc, f1))
with open(path + 'score.txt', "w") as f:
    f.write("acc : " + str(acc) + '\n')
    f.write("f1 : " + str(f1) + '\n')
    f.write("score : " + get_score(acc, f1))
