import math
from openpyxl import Workbook
from math import cos, sin

# 创建一个Workbook对象
workbook = Workbook()


class T2_model():
    def __init__(self, θ, α, H, distance=None):
        self.θ = θ
        self.α = α
        self.H = H
        self.distance = distance

    def get_sinslope(self, betas):
        alpha = self.α
        ans = []
        for beta in betas:
            if beta == 0:
                result = 0
                ans.append(result)
            else:
                x = math.cos(alpha) / (math.sin(alpha) * math.sin(beta))
                result = 1 / math.sqrt(1 + x ** 2)
                ans.append(result)

        return ans

    def get_slope(self, betas):
        # 返回值为弧度值
        alpha = self.α
        ans = []
        for beta in betas:
            if beta == 0:
                result = 0
                ans.append(result)
            else:
                x = math.cos(alpha) / (math.sin(alpha) * math.sin(beta))
                result = 1 / math.sqrt(1 + x ** 2)
                ans.append(math.asin(result))

        return ans

    def get_gamma1(self, betas):
        # 返回值为 γ 弧度值
        alpha = self.α
        ans = []
        for beta in betas:
            try:
                denominator = (math.sin(alpha) * math.cos(beta))
                if denominator == 0:
                    raise ZeroDivisionError
                x = math.cos(alpha) / denominator
                result = 1 / math.sqrt(1 + x ** 2)
            except ValueError:
                result = 0
            except ZeroDivisionError:
                result = 0
            ans.append(math.asin(result))
        return ans

    def get_gamma2(self, betas):
        # 返回值为 γ‘ 弧度值
        alpha = self.α
        ans = []
        for beta in betas:
            try:
                denominator = (math.sin(alpha) * math.sin(beta))
                if denominator == 0:
                    raise ZeroDivisionError
                x = math.cos(alpha) / denominator
                result = 1 / math.sqrt(1 + x ** 2)
            except ValueError:
                result = 0
            except ZeroDivisionError:
                result = 0
            ans.append(math.asin(result))
        return ans

    def deep_calculate(self, distance=None, gamma=None, beta=None):
        if distance is None:
            distance = self.distance
        D = []  # 海水深度
        for i in range(len(gamma)):
            dt = []
            for item in self.distance:
                d = self.H - (item * sin(gamma[i]) * (-cos(beta[i])) / cos(gamma[i]) * abs(cos(beta[i])))
                dt.append(d)
            D.append(dt)
        return D

    def width_calculate(self, Deepth=None, gamma=None):
        W = []  # 覆盖宽度
        X = []  # 靠近负方向覆盖宽度
        Y = []  # 靠近正方形覆盖宽度
        for i in range(len(Deepth)):
            w = []
            x_list = []
            y_list = []
            for d in Deepth[i]:
                x = d * sin(self.θ / 2) / cos(self.θ / 2 + gamma[i])
                y = d * sin(self.θ / 2) / sin(self.θ / 2 - gamma[i])
                x_list.append(x)
                y_list.append(y)
                w.append(x + y)
            X.append(x_list)
            Y.append(y_list)
            W.append(w)
        return W, X, Y


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

# for item in deep:
#     print(item)
# print(angles)
width, X, Y = ans.width_calculate(Deepth=deep, gamma=gamma2)
# for item in width:
#     print(item)
format_width = []
format_d = []
for dt in deep:
    t = []
    for item in dt:
        tmp = "{:.2f}".format(item)
        t.append(tmp)
    format_d.append(t)
for widt in width:
    t = []
    for item in widt:
        tmp = "{:.2f}".format(item)
        t.append(tmp)
    format_width.append(t)
for item in format_width:
    print(item)

# for item in format_d:
#     print(item)
for row in format_width:
    sheet.append(row)

# 保存Excel文件
workbook.save('T2-output-format.xlsx')
