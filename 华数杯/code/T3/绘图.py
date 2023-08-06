import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("../../dataset/demo.xlsx")
df = df.drop(df.tail(20).index)
df = df.iloc[:, 6:10]

selected_0 = df[df['婴儿行为特征'] == '中等型'].drop('婴儿行为特征', axis=1).values.reshape(3, 225)
selected_1 = df[df['婴儿行为特征'] == '安静型'].drop('婴儿行为特征', axis=1).values.reshape(3, 120)
selected_2 = df[df['婴儿行为特征'] == '矛盾型'].drop('婴儿行为特征', axis=1).values.reshape(3, 45)

plt.rcParams['font.sans-serif'] = ['SimSun']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(selected_0[0], selected_0[1], selected_0[2], c='r', label='中等型')
# ax.scatter(selected_1[0], selected_1[1], selected_1[2], c='g', label='安静型')
ax.scatter(selected_2[0], selected_2[1], selected_2[2], c='b', label='矛盾型')

# 设置标题和轴标签
ax.set_title('中-矛散点图')
ax.set_xlabel('CBTS')
ax.set_ylabel('EPDS')
ax.set_zlabel('HADS')
ax.legend()
plt.show()
