import numpy as np
from scipy import interp


def accuracy_score(y_true, y_pred):
    correct = np.sum(y_true == y_pred)
    total = len(y_true)
    accuracy = correct / total
    return accuracy


def precision_score(y_true, y_pred):
    true_positives = np.sum((y_true == 1) & (y_pred == 1))
    false_positives = np.sum((y_true == 0) & (y_pred == 1))
    precision = true_positives / (true_positives + false_positives)
    return precision


def recall_score(y_true, y_pred):
    true_positives = np.sum((y_true == 1) & (y_pred == 1))
    false_negatives = np.sum((y_true == 1) & (y_pred == 0))
    recall = true_positives / (true_positives + false_negatives)
    return recall


def f1_score(y_true, y_pred):
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1


import numpy as np
from scipy import interp


def roc_curve(y_true, y_scores):
    # 将真实标签和预测概率按照预测概率降序排序
    sorted_indices = np.argsort(y_scores)[::-1]
    y_true_sorted = y_true[sorted_indices]
    y_scores_sorted = y_scores[sorted_indices]

    # 初始化真正率（TPR）和假正率（FPR）的列表
    tpr = [0]
    fpr = [0]
    thresholds = []

    # 统计正例和负例的数量
    num_positives = np.sum(y_true)
    num_negatives = len(y_true) - num_positives

    # 计算真正率（TPR）和假正率（FPR）
    for i in range(len(y_scores_sorted)):
        if y_true_sorted[i] == 1:
            tpr.append(tpr[-1] + 1 / num_positives)
            fpr.append(fpr[-1])
        else:
            fpr.append(fpr[-1] + 1 / num_negatives)
            tpr.append(tpr[-1])
        thresholds.append(y_scores_sorted[i])

    return np.array(fpr), np.array(tpr), np.array(thresholds)


def auc(fpr, tpr):
    # 使用梯形法则计算曲线下面积（AUC）
    return np.trapz(tpr, fpr)
