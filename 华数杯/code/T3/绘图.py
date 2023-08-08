import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("../../dataset/demo.xlsx")
df = df.drop(df.tail(20).index)
df = df.iloc[:, 6:10]

selected_0 = df[df['婴儿行为特征'] == '中等型'].drop('婴儿行为特征', axis=1)
selected_1 = df[df['婴儿行为特征'] == '安静型'].drop('婴儿行为特征', axis=1)
selected_2 = df[df['婴儿行为特征'] == '矛盾型'].drop('婴儿行为特征', axis=1)
selected_0_x = selected_0['CBTS']
selected_0_y = selected_0['EPDS']
selected_0_z = selected_0['HADS']

selected_1_x = selected_1['CBTS']
selected_1_y = selected_1['EPDS']
selected_1_z = selected_1['HADS']

selected_2_x = selected_2['CBTS']
selected_2_y = selected_2['EPDS']
selected_2_z = selected_2['HADS']
plt.rcParams['font.sans-serif'] = ['SimSun']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(selected_0_x, selected_0_y, selected_0_z, c='r', label='中等型')
ax.scatter(selected_1_x, selected_1_y, selected_1_z, c='g', label='安静型')
ax.scatter(selected_2_x, selected_2_y, selected_2_z, c='b', label='矛盾型')

# 设置标题和轴标签
ax.set_title('分布散点图')
ax.set_xlabel('CBTS')
ax.set_ylabel('EPDS')
ax.set_zlabel('HADS')
ax.legend()
plt.show()
