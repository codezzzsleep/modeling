import numpy as np
import pygrey

# 原始数据
data = np.array([10, 15, 20, 25, 30, 35, 40])

# 创建灰色模型对象
model = pygrey

# 拟合模型
model.fit(data)

# 进行预测
prediction = model.predict(steps=3)

# 打印预测结果
print("预测结果:", prediction)
