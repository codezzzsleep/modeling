import sympy as sp
from sympy import sin, cos, sqrt, solve, S, symbols, pi
from sympy import latex


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

result = [(deep[i] + deep[i + 1]) / 2 for i in range(len(deep) - 1)]

res = []
ans = []
beta = sp.symbols('beta')

for d in result:
    h = cos(α_rad) / (sin(α_rad) * cos(beta) * sqrt(1 + (cos(α_rad) / (sin(α_rad) * cos(beta))) ** 2))

    w = ((2 * d + (sin(α_rad) * cos(beta)) / cos(α_rad)) * sin(θ_rad / 2)) / (
            cos(θ_rad / 2) * cos(beta) - sin(θ_rad / 2) * sin(beta)
    ) + ((2 * d + (sin(α_rad) * cos(beta)) / cos(α_rad)) * sin(θ_rad / 2)) / (
                cos(θ_rad / 2) * cos(beta) + sin(θ_rad / 2) * sin(beta))
    f = w * h / 2

    f_derivative = sp.diff(f, beta)
    # beta_solutions = solve(f_derivative, beta)
    # print("beta 的解：", beta_solutions)
    print("导数：", f_derivative)
    res.append(f_derivative)
    # ans.append(beta_solutions)
beta = symbols('beta')
frac_pi = S(1) / 120
replacements = [(0.00833333333333333 * pi, frac_pi * pi)]

latex_derivatives = []
for d in res:
    derivative_expr = sp.sympify(d).subs(replacements)
    latex_derivatives.append(latex(derivative_expr))

for i, latex_derivative in enumerate(latex_derivatives):
    print(f"导数 {i+1}:")
    print(f"${latex_derivative}$")
    print()