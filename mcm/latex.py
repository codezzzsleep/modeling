from sympy import S, symbols, pi, sin, cos, sqrt
from sympy import latex
import sympy

beta = symbols('beta')
frac_pi = S(1) / 120  # 将分数形式的 PI 倍数表示为分数

derivatives = [
    (sqrt(3) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 5556 * sin(
        0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                 2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2)) + sqrt(3) * (
                 sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 5556 * sin(
             0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                 2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2))) * sin(beta) * cos(0.00833333333333333 * pi) / (
                2 * sqrt(
            1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) * sin(
            0.00833333333333333 * pi) * cos(beta) ** 2) + (-sqrt(3) * sin(0.00833333333333333 * pi) * sin(beta) / (
                2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2) * cos(0.00833333333333333 * pi)) + sqrt(3) * (
                                                                       sin(beta) / 2 - sqrt(3) * cos(beta) / 2) * (
                                                                       sin(0.00833333333333333 * pi) * cos(beta) / cos(
                                                                   0.00833333333333333 * pi) + 5556 * sin(
                                                                   0.00833333333333333 * pi) / cos(
                                                                   0.00833333333333333 * pi) + 220) / (2 * (
                sqrt(3) * sin(beta) / 2 + cos(beta) / 2) ** 2) - sqrt(3) * sin(0.00833333333333333 * pi) * sin(beta) / (
                                                                       2 * (-sqrt(3) * sin(beta) / 2 + cos(
                                                                   beta) / 2) * cos(0.00833333333333333 * pi)) + sqrt(
        3) * (sin(beta) / 2 + sqrt(3) * cos(beta) / 2) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(
        0.00833333333333333 * pi) + 5556 * sin(0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (2 * (
                -sqrt(3) * sin(beta) / 2 + cos(beta) / 2) ** 2)) * cos(0.00833333333333333 * pi) / (2 * sqrt(
        1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) * sin(
        0.00833333333333333 * pi) * cos(beta)) - (sqrt(3) * (
                sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 5556 * sin(
            0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                                                              2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2)) + sqrt(
        3) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 5556 * sin(
        0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                                                              2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2))) * sin(
        beta) * cos(0.00833333333333333 * pi) ** 3 / (2 * (
                1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) ** (
                                                                  3 / 2) * sin(0.00833333333333333 * pi) ** 3 * cos(
        beta) ** 4)
    (sqrt(3) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 1852 * sin(
        0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                 2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2)) + sqrt(3) * (
                 sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 1852 * sin(
             0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                 2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2))) * sin(beta) * cos(0.00833333333333333 * pi) / (
                2 * sqrt(
            1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) * sin(
            0.00833333333333333 * pi) * cos(beta) ** 2) + (-sqrt(3) * sin(0.00833333333333333 * pi) * sin(beta) / (
                2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2) * cos(0.00833333333333333 * pi)) + sqrt(3) * (
                                                                       sin(beta) / 2 - sqrt(3) * cos(beta) / 2) * (
                                                                       sin(0.00833333333333333 * pi) * cos(beta) / cos(
                                                                   0.00833333333333333 * pi) + 1852 * sin(
                                                                   0.00833333333333333 * pi) / cos(
                                                                   0.00833333333333333 * pi) + 220) / (2 * (
                sqrt(3) * sin(beta) / 2 + cos(beta) / 2) ** 2) - sqrt(3) * sin(0.00833333333333333 * pi) * sin(beta) / (
                                                                       2 * (-sqrt(3) * sin(beta) / 2 + cos(
                                                                   beta) / 2) * cos(0.00833333333333333 * pi)) + sqrt(
        3) * (sin(beta) / 2 + sqrt(3) * cos(beta) / 2) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(
        0.00833333333333333 * pi) + 1852 * sin(0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (2 * (
                -sqrt(3) * sin(beta) / 2 + cos(beta) / 2) ** 2)) * cos(0.00833333333333333 * pi) / (2 * sqrt(
        1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) * sin(
        0.00833333333333333 * pi) * cos(beta)) - (sqrt(3) * (
                sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 1852 * sin(
            0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                                                              2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2)) + sqrt(
        3) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 1852 * sin(
        0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                                                              2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2))) * sin(
        beta) * cos(0.00833333333333333 * pi) ** 3 / (2 * (
                1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) ** (
                                                                  3 / 2) * sin(0.00833333333333333 * pi) ** 3 * cos(
        beta) ** 4)
    (sqrt(3) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) - 1852 * sin(
        0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                 2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2)) + sqrt(3) * (
                 sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) - 1852 * sin(
             0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                 2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2))) * sin(beta) * cos(0.00833333333333333 * pi) / (
                2 * sqrt(
            1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) * sin(
            0.00833333333333333 * pi) * cos(beta) ** 2) + (-sqrt(3) * sin(0.00833333333333333 * pi) * sin(beta) / (
                2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2) * cos(0.00833333333333333 * pi)) + sqrt(3) * (
                                                                       sin(beta) / 2 - sqrt(3) * cos(beta) / 2) * (
                                                                       sin(0.00833333333333333 * pi) * cos(beta) / cos(
                                                                   0.00833333333333333 * pi) - 1852 * sin(
                                                                   0.00833333333333333 * pi) / cos(
                                                                   0.00833333333333333 * pi) + 220) / (2 * (
                sqrt(3) * sin(beta) / 2 + cos(beta) / 2) ** 2) - sqrt(3) * sin(0.00833333333333333 * pi) * sin(beta) / (
                                                                       2 * (-sqrt(3) * sin(beta) / 2 + cos(
                                                                   beta) / 2) * cos(0.00833333333333333 * pi)) + sqrt(
        3) * (sin(beta) / 2 + sqrt(3) * cos(beta) / 2) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(
        0.00833333333333333 * pi) - 1852 * sin(0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (2 * (
                -sqrt(3) * sin(beta) / 2 + cos(beta) / 2) ** 2)) * cos(0.00833333333333333 * pi) / (2 * sqrt(
        1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) * sin(
        0.00833333333333333 * pi) * cos(beta)) - (sqrt(3) * (
                sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) - 1852 * sin(
            0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                                                              2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2)) + sqrt(
        3) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) - 1852 * sin(
        0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                                                              2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2))) * sin(
        beta) * cos(0.00833333333333333 * pi) ** 3 / (2 * (
                1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) ** (
                                                                  3 / 2) * sin(0.00833333333333333 * pi) ** 3 * cos(
        beta) ** 4)
    (sqrt(3) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) - 5556 * sin(
        0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                 2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2)) + sqrt(3) * (
                 sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) - 5556 * sin(
             0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                 2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2))) * sin(beta) * cos(0.00833333333333333 * pi) / (
                2 * sqrt(
            1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) * sin(
            0.00833333333333333 * pi) * cos(beta) ** 2) + (-sqrt(3) * sin(0.00833333333333333 * pi) * sin(beta) / (
                2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2) * cos(0.00833333333333333 * pi)) + sqrt(3) * (
                                                                       sin(beta) / 2 - sqrt(3) * cos(beta) / 2) * (
                                                                       sin(0.00833333333333333 * pi) * cos(beta) / cos(
                                                                   0.00833333333333333 * pi) - 5556 * sin(
                                                                   0.00833333333333333 * pi) / cos(
                                                                   0.00833333333333333 * pi) + 220) / (2 * (
                sqrt(3) * sin(beta) / 2 + cos(beta) / 2) ** 2) - sqrt(3) * sin(0.00833333333333333 * pi) * sin(beta) / (
                                                                       2 * (-sqrt(3) * sin(beta) / 2 + cos(
                                                                   beta) / 2) * cos(0.00833333333333333 * pi)) + sqrt(
        3) * (sin(beta) / 2 + sqrt(3) * cos(beta) / 2) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(
        0.00833333333333333 * pi) - 5556 * sin(0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (2 * (
                -sqrt(3) * sin(beta) / 2 + cos(beta) / 2) ** 2)) * cos(0.00833333333333333 * pi) / (2 * sqrt(
        1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) * sin(
        0.00833333333333333 * pi) * cos(beta)) - (sqrt(3) * (
                sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) - 5556 * sin(
            0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                                                              2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2)) + sqrt(
        3) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) - 5556 * sin(
        0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                                                              2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2))) * sin(
        beta) * cos(0.00833333333333333 * pi) ** 3 / (2 * (
                1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) ** (
                                                                  3 / 2) * sin(0.00833333333333333 * pi) ** 3 * cos(
        beta) ** 4)

]

# 用分数替换表达式中的浮点数（0.00833333333333333*pi -> frac_pi*pi）
replacements = [(0.00833333333333333 * pi, frac_pi * pi)]

latex_derivatives = []

for d in derivatives:
    derivative_expr = sympy.sympify(d).subs(replacements)
    latex_derivatives.append(latex(derivative_expr))

for latex_derivative in latex_derivatives:
    print(latex_derivative)
