from model import T2_model
import math
from openpyxl import Workbook

# 创建一个Workbook对象
workbook = Workbook()

# 获取默认的工作表
sheet = workbook.active
θ = math.radians(120)
α = math.radians(1.5)
H = 120
distance = [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1]
bates = [0, 45, 90, 135, 180, 225, 270, 315]
Conversion = 1852
for i in range(len(distance)):
    distance[i] = distance[i] * Conversion
for i in range(len(bates)):
    bates[i] = math.radians(bates[i])

ans = T2_model(θ, α, H, distance)
# γ
gamma1 = ans.get_gamma1(betas=bates)
# γ’
gamma2 = ans.get_gamma2(betas=bates)

deep = ans.deep_calculate(distance, gamma1, bates)

width, X, Y = ans.width_calculate(Deepth=deep, gamma=gamma2)
result = []
for i in range(len(width)-1):
    a = []
    for j in range(len(width)-1):
        tmp1 = width[i][j] + width[i][j + 1]
        h = (distance[i + 1] - distance[i]) / math.cos(gamma1[j + 1])
        a.append(tmp1 * h / 2)
    tmp1 = width[i][7] + width[i][0]
    h = (distance[i + 1] - distance[i]) / math.cos(gamma1[i + 1])
    a.append(tmp1 * h / 2)
    result.append(a)
# for item in result:
#     print(item)
format_result = []
for res in result:
    t = []
    for item in res:
        tmp = "{:.2f}".format(item)
        t.append(tmp)
    format_result.append(t)
for item in format_result:
    print(item)
for row in format_result:
    sheet.append(row)

# 保存Excel文件
workbook.save('T3-output-format.xlsx')
