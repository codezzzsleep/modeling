import numpy as np

# 原始数组
arr = np.array([0, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1])

# 计算每个元素的频率
unique, counts = np.unique(arr, return_counts=True)

# 根据频率排序元素
sorted_indices = np.argsort(-counts)
sorted_elements = unique[sorted_indices]

# 创建替换字典
replace_dict = {sorted_elements[i]: i for i in range(len(sorted_elements))}

# 替换数组中的元素
arr_replaced = np.vectorize(replace_dict.get)(arr)

print(arr_replaced)
