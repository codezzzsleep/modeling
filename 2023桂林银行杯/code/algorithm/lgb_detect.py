import lightgbm as lgb
import numpy as np
import pandas as pd
from util.data_process import fix_test_dataset
from util.data_process import fix_train_dataset
from util.data_storage import detect_make_dir
from util.data_define import get_features


feature_select = "impl12"
features = get_features(feature_select)
label_column = ['label']
detect_dir = detect_make_dir()
pre_path = "../run/detect/" + str(detect_dir) + "/" + "pre_" + feature_select
pre_pro_path = "../run/detect/" + str(detect_dir) + "/" + "pre_pro_" + feature_select
train, label = fix_train_dataset(features, label_column)
clf = lgb.train()
