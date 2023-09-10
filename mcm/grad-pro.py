import sympy as sp
from sympy import sin, cos, sqrt, solve


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


θ_val, α_val = 120, 1.5
θ, α = sp.symbols('θ α')
H = 110
# 计算弧度制的角度
θ_rad = sp.rad(θ_val).subs(θ, θ_val)
α_rad = sp.rad(α_val).subs(α, α_val)

distance = [-2, -1, 0, 1, 2]
Conversion = 1852
for i in range(len(distance)):
    distance[i] = distance[i] * Conversion

ans = T1_model(θ_rad, α_rad, H, distance)
deep = ans.deep_calculate()

res = []
beta = sp.symbols('beta')
beta_solutions = []

for d in deep:
    h = cos(α_rad) / (sin(α_rad) * cos(beta) * sqrt(1 + (cos(α_rad) / (sin(α_rad) * cos(beta))) ** 2))

    w = ((2 * d + (sin(α_rad) * cos(beta)) / cos(α_rad)) * sin(θ_rad / 2)) / (
            cos(θ_rad / 2) * cos(beta) - sin(θ_rad / 2) * sin(beta)
    ) + ((2 * d + (sin(α_rad) * cos(beta)) / cos(α_rad)) * sin(θ_rad / 2)) / (
                cos(θ_rad / 2) * cos(beta) + sin(θ_rad / 2) * sin(beta))
    f = w * h / 2

    f_derivative = sp.diff(f, beta)
    print("导数：", f_derivative)
    res.append(f_derivative)

    # 求梯度为零的解
    solutions = solve(f_derivative, beta)
    beta_solutions.append(solutions)

print("beta 的解：", beta_solutions)
