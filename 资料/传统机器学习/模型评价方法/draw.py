from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import roc_curve, auc
from detaile import roc_curve, auc
import matplotlib.pyplot as plt

# 加载 breast_cancer 数据集
data = load_breast_cancer()
X = data.data
y = data.target

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练逻辑回归模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 获取测试集上的预测概率
y_scores = model.predict_proba(X_test)[:, 1]

# 计算真正率（TPR）、假正率（FPR）和阈值（thresholds）
fpr, tpr, thresholds = roc_curve(y_test, y_scores)

# 计算曲线下面积（AUC）
roc_auc = auc(fpr, tpr)

# 绘制 ROC 曲线
plt.plot(fpr, tpr, label='ROC curve (AUC = %0.2f)' % roc_auc)

# 绘制对角线
plt.plot([0, 1], [0, 1], 'k--')

# 添加图例
plt.legend()

# 添加标题和轴标签
plt.title('Receiver Operating Characteristic')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.savefig("logs/roc.png")
# 显示图形
plt.show()
