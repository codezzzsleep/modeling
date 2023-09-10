import math
from math import sin, cos, sqrt


class T1_model():
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
                print(f"重叠宽度：{tmp4}")
                if tmp4 < 0:  # 如果重叠宽度小于 0 则设为 0 表示没有覆盖
                    r = 0
                else:
                    r = (tmp4 / W[i + 1])
                Rate.append(r)
        return Rate


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
