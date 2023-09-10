import pandas as pd

# 读取CSV文件
data = pd.read_csv("data.csv")

# 提取A区域数据
a_region = data.iloc[150:201, 0:101]

# 提取B1区域数据
b1_region = data.iloc[100:151, 0:131]

# 提取B2区域数据
b2_region = data.iloc[150:251, 100:131]

# 提取C1区域数据
c1_region = data.iloc[0:101, 0:201]

# 提取C2区域数据
c2_region = data.iloc[100:251, 130:201]

# A区域描述性统计
a_stats = a_region.describe()

# B1区域描述性统计
b1_stats = b1_region.describe()

# B2区域描述性统计
b2_stats = b2_region.describe()

# C1区域描述性统计
c1_stats = c1_region.describe()

# C2区域描述性统计
c2_stats = c2_region.describe()

# 打印结果
print("A区域描述性统计:")
print(a_stats)
print("\nB1区域描述性统计:")
print(b1_stats)
print("\nB2区域描述性统计:")
print(b2_stats)
print("\nC1区域描述性统计:")
print(c1_stats)
print("\nC2区域描述性统计:")
print(c2_stats)
