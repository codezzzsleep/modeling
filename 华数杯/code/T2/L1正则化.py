from sklearn.linear_model import Lasso
import pandas as pd

# 创建一个Lasso回归模型对象
lasso = Lasso(alpha=0.001)

# 假设X是特征矩阵，y是目标变量
df = pd.read_excel("../../dataset/demo_train.xlsx")
type_counts = df['婴儿行为特征'].value_counts()
print(type_counts)
X = df.iloc[:-20, 1:9].to_numpy()
y = df.iloc[:-20, 9].to_numpy()

# 拟合模型
lasso.fit(X, y)

# 预测
y_pred = lasso.predict(X)

# 打印模型系数和预测结果
print("模型系数:", lasso.coef_)
print("预测结果:", y_pred)
