from sympy import symbols, sin, cos, solve, sqrt, pi

# 定义符号变量
beta = symbols('beta')

# 定义导数表达式
derivative_expr = (sqrt(3) * (sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 5556 * sin(
    0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                           2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2)) + sqrt(3) * (
                           sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 5556 * sin(
                       0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                           2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2))) * sin(beta) * cos(
    0.00833333333333333 * pi) / (2 * sqrt(
    1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) * sin(
    0.00833333333333333 * pi) * cos(beta) ** 2) + (-sqrt(3) * sin(0.00833333333333333 * pi) * sin(beta) / (
        2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2) * cos(0.00833333333333333 * pi)) + sqrt(3) * (
                                                           sin(beta) / 2 - sqrt(3) * cos(beta) / 2) * (
                                                           sin(0.00833333333333333 * pi) * cos(beta) / cos(
                                                       0.00833333333333333 * pi) + 5556 * sin(
                                                       0.00833333333333333 * pi) / cos(
                                                       0.00833333333333333 * pi) + 220) / (2 * (
        sqrt(3) * sin(beta) / 2 + cos(beta) / 2) ** 2) - sqrt(3) * sin(0.00833333333333333 * pi) * sin(beta) / (
                                                           2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2) * cos(
                                                       0.00833333333333333 * pi)) + sqrt(3) * (
                                                           sin(beta) / 2 + sqrt(3) * cos(beta) / 2) * (
                                                           sin(0.00833333333333333 * pi) * cos(beta) / cos(
                                                       0.00833333333333333 * pi) + 5556 * sin(
                                                       0.00833333333333333 * pi) / cos(
                                                       0.00833333333333333 * pi) + 220) / (2 * (
        -sqrt(3) * sin(beta) / 2 + cos(beta) / 2) ** 2)) * cos(0.00833333333333333 * pi) / (2 * sqrt(
    1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) * sin(
    0.00833333333333333 * pi) * cos(beta)) - (sqrt(3) * (
        sin(0.00833333333333333 * pi) * cos(beta) / cos(0.00833333333333333 * pi) + 5556 * sin(
    0.00833333333333333 * pi) / cos(0.00833333333333333 * pi) + 220) / (
                                                      2 * (sqrt(3) * sin(beta) / 2 + cos(beta) / 2)) + sqrt(3) * (
                                                      sin(0.00833333333333333 * pi) * cos(beta) / cos(
                                                  0.00833333333333333 * pi) + 5556 * sin(
                                                  0.00833333333333333 * pi) / cos(
                                                  0.00833333333333333 * pi) + 220) / (
                                                      2 * (-sqrt(3) * sin(beta) / 2 + cos(beta) / 2))) * sin(
    beta) * cos(0.00833333333333333 * pi) ** 3 / (2 * (
        1 + cos(0.00833333333333333 * pi) ** 2 / (sin(0.00833333333333333 * pi) ** 2 * cos(beta) ** 2)) ** (
                                                          3 / 2) * sin(0.00833333333333333 * pi) ** 3 * cos(
    beta) ** 4)

# 求解导数为0的解
solutions = solve(derivative_expr, beta)

# 打印解
print("当导数为0时，beta的值为:")
for sol in solutions:
    print(sol.evalf())
