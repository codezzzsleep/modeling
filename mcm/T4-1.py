from math import sin, cos
import math


class T4_model():
    def __init__(self, θ, α, H, distance=None):
        self.θ = θ
        self.α = α
        self.H = H
        self.distance = distance

    def deep_calculate(self, distance=None):
        if distance is None:
            distance = self.distance
        D = []  # 海水深度
        for item in self.distance:
            d = self.H - (item * sin(self.α) / cos(self.α))
            D.append(d)
        return D

    def width_calculate(self, distance=None, D=None):
        if distance is None:
            distance = self.distance
        W = []  # 覆盖宽度
        X = []  # 靠近负方向覆盖宽度
        Y = []  # 靠近正方形覆盖宽度
        if D is None:
            return None

        for d in D:
            x = d * sin(self.θ / 2) / cos(self.θ / 2 + self.α)
            y = d * sin(self.θ / 2) / sin(self.θ / 2 - self.α)
            X.append(x)
            Y.append(y)
            W.append(x + y)
        return W, X, Y

    def overlap_calculate(self, distance=None, W=None, X=None, Y=None):
        if distance is None:
            distance = self.distance
        if W is None:
            return None
        if X is None:
            return None
        if Y is None:
            return None
        else:
            Rate = []  # 重叠率
            for i in range(len(self.distance) - 1):
                tmp1 = (self.distance[i + 1] - self.distance[i]) / cos(self.α)  # 两测线中心点距在斜坡上的投影
                tmp2 = X[i]  # 覆盖宽度中正方向的那一部分
                tmp3 = Y[i + 1]  # 覆盖宽度中负方向的那一部分
                tmp4 = tmp3 + tmp2 - tmp1  # 重叠的宽度
                if tmp4 < 0:  # 如果重叠宽度小于 0 则设为 0 表示没有覆盖
                    r = 0
                else:
                    r = (tmp4 / W[i + 1])
                Rate.append(r)
        return Rate


θ = math.radians(120)
α = math.radians(1.5)
H = 110
distance = [-2, 0, 2]
Conversion = 1852
for i in range(len(distance)):
    distance[i] = distance[i] * Conversion
ans = T4_model(θ, α, H, distance)
distance.append(3679.21)
deep = ans.deep_calculate()
print(deep)
import math
from sympy import symbols, Eq, solve, sin, cos

alpha = math.radians(1.5)
the = math.radians(60)

# 定义未知数
d = symbols('d')

# 定义方程
equation = Eq(3704 + d, (110 - d * sin(alpha) / cos(alpha)) * sin(the) / cos(alpha + the))

# 求解方程
solution = solve(equation, d)

# 输出解
print(solution)
ans_distance = []
ans_distance.append(solution[0])

for i in range(41):
    # 定义未知数
    d = symbols('d')
    d1 = ans_distance[i]
    Y1 = (110 - d1 * sin(alpha) / cos(alpha)) * sin(the) / cos(the - alpha)
    X2 = (110 - d * sin(alpha) / cos(alpha)) * sin(the) / cos(the + alpha)
    detl = (d - d1) / cos(alpha)
    # 定义方程
    equation = Eq((Y1 + X2 - detl) / detl, 0.343)

    # 求解方程
    solution = solve(equation, d)
    ans_distance.append(solution[0])
print(ans_distance)
