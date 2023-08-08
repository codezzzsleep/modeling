import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../../dataset/k-means.csv')

class_1 = df[df['聚类种类'] == '类别1'].drop('聚类种类', axis=1)
class_2 = df[df['聚类种类'] == '类别2'].drop('聚类种类', axis=1)
class_3 = df[df['聚类种类'] == '类别3'].drop('聚类种类', axis=1)
class_4 = df[df['聚类种类'] == '类别4'].drop('聚类种类', axis=1)

class_1_x = class_1['整晚睡眠时间（时：分：秒）'].to_numpy()
class_1_y = class_1['睡醒次数'].to_numpy()
class_1_z = class_1['入睡方式'].to_numpy()

class_2_x = class_2['整晚睡眠时间（时：分：秒）'].to_numpy()
class_2_y = class_2['睡醒次数'].to_numpy()
class_2_z = class_2['入睡方式'].to_numpy()

class_3_x = class_3['整晚睡眠时间（时：分：秒）'].to_numpy()
class_3_y = class_3['睡醒次数'].to_numpy()
class_3_z = class_3['入睡方式'].to_numpy()

class_4_x = class_4['整晚睡眠时间（时：分：秒）'].to_numpy()
class_4_y = class_4['睡醒次数'].to_numpy()
class_4_z = class_4['入睡方式'].to_numpy()
plt.rcParams['font.sans-serif'] = ['SimSun']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 生成随机数据


# 绘制三维散点图
ax.scatter(class_1_x, class_1_y, class_1_z, c='r', label='类别1')
ax.scatter(class_2_x, class_2_y, class_2_z, c='g', label='类别2')
ax.scatter(class_3_x, class_3_y, class_3_z, c='b', label='类别3')
ax.scatter(class_4_x, class_4_y, class_4_z, c='m', label='类别4')
# 设置坐标轴标签
ax.set_xlabel('整晚睡眠时间（时：分：秒）')
ax.set_ylabel('睡醒次数')
ax.set_zlabel('入睡方式')
ax.legend()
# 显示图形
plt.show()
