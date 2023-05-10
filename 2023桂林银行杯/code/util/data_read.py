import warnings
import pandas as pd


warnings.simplefilter('ignore')
# 读取训练数据
ass_train = pd.read_csv('../../data/train/asset_train.csv')
bhv_train = pd.read_csv('../../data/train/bhv_train.csv')
cust_train = pd.read_csv('../../data/train/cust_train.csv')
train_label = pd.read_csv('../../data/train/train_label.csv')
loan_train = pd.read_csv('../../data/train/loan_train.csv')
trans_train = pd.read_csv('../../data/train/trans_train.csv')

ass_test = pd.read_csv('../../data/test/asset_test.csv')
bhv_test = pd.read_csv('../../data/test/bhv_test.csv')
cust_test = pd.read_csv('../../data/test/cust_test.csv')
loan_test = pd.read_csv('../../data/test/loan_test.csv')
trans_test = pd.read_csv('../../data/test/trans_test.csv')
# 拼接完整训练集
train = cust_train.merge(loan_train, on='id', how='left')
train = train.merge(trans_train, on='id', how='left')
train = train.merge(bhv_train, on='id', how='left')
train = train.merge(ass_train, on='id', how='left')
train = train.merge(train_label, on='id', how='left')

# print(train)
# print(len(train))
# 拼接完整测试集
test = cust_test.merge(loan_test, on='id', how='left')
test = test.merge(trans_test, on='id', how='left')
test = test.merge(bhv_test, on='id', how='left')
test = test.merge(ass_test, on='id', how='left')
# 导出训练集和测试集
train.to_csv('train.csv')
test.to_csv('test.csv')
