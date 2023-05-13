import pandas as pd
import numpy as np


def fix_train_dataset(features, label_column):
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
    return train, label
def fix_test_dataset(features):
    test_data = pd.read_csv("../data/test.csv")
    test = test_data[features]
    test = pd.get_dummies(test)
    tmp = np.isnan(test).any()
    fill_column = []
    for idx in tmp.index:
        if tmp[idx]:
            fill_column.append(idx)
    test[fill_column] = test[fill_column].fillna(test[fill_column].median())
    return test
