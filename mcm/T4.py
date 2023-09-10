import csv

# 读取原始的 CSV 文件
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# 提取 x 坐标值（第一行除第一个元素）
x_values = [float(value) for value in data[0][1:]]

# 提取 y 坐标值（第一列除第一个元素）
y_values = [float(row[0]) for row in data[1:]]

# 创建 (x, y, z) 对
xyz_pairs = []
for i, row in enumerate(data[1:]):
    for j, value in enumerate(row[1:]):
        x = x_values[j]
        y = y_values[i]
        z = float(value)
        xyz_pairs.append((x, y, z))

# 打印生成的 (x, y, z) 对
for pair in xyz_pairs:
    print(pair)

# 保存 (x, y, z) 对到新的 CSV 文件
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(xyz_pairs)
