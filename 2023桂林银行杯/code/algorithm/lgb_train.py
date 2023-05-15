import lightgbm as lgb
from lightgbm import log_evaluation, early_stopping
import numpy as np
import pandas as pd
from util.data_process import fix_test_dataset
from util.data_process import fix_train_dataset
from util.data_storage import train_make_dir
from util.data_define import get_features
from sklearn.model_selection import train_test_split

feature_select = 'all'
features = get_features(feature_select)
label_column = ['label']
train_dir = train_make_dir()
path = "../run/train/" + str(train_dir) + "/"
pre_path = "../run/train/" + str(train_dir) + "/" + "pre_" + feature_select
pre_pro_path = "../run/train/" + str(train_dir) + "/" + "pre_pro_" + feature_select
train_data, train_target = fix_train_dataset(features, label_column)
train_X, test_X, train_y, test_y = train_test_split(train_data, train_target, test_size=0.5)

lgb_train = lgb.Dataset(train_X, train_y)
lgb_eval = lgb.Dataset(test_X, test_y, reference=lgb_train)

params = {
    'learning_rate': 0.01,
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': 'auc',
    'num_leaves': 63,
    'feature_fraction': 0.8,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'seed': 2,
    'bagging_seed': 1,
    'feature_fraction_seed': 7,
    'min_data_in_leaf': 20,
    'verbose': -1,
    'n_jobs': 4
}


clf = lgb.train(
            params,
            lgb_train,
            num_boost_round=10000,
            valid_sets=[lgb_eval],
            early_stopping_rounds=100,
            verbose_eval=100, )
clf.save_model(path + "best.txt")
