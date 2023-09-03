import numpy as np


# 目标函数：f(x) = x^2
def target_function(x):
    return x ** 2


# 模拟退火算法的实现
def simulated_annealing(initial_temperature, cooling_rate, initial_solution, iter_per_temp):
    current_solution = initial_solution
    current_temperature = initial_temperature

    # 当前温度大于1时，循环执行
    while current_temperature > 1:
        # 对每个温度层执行固定次数的迭代
        for i in range(iter_per_temp):
            # 在邻域内生成新解
            new_solution = current_solution + np.random.uniform(-1, 1)

            # 根据目标函数确定解的优劣
            cost_difference = target_function(current_solution) - target_function(new_solution)

            # 若新解更优，接受新解；若次优，在一定概率下接受新解
            if cost_difference > 0 or np.random.uniform(0, 1) < np.exp(cost_difference / current_temperature):
                current_solution = new_solution

        # 降温
        current_temperature *= cooling_rate

    return current_solution


if __name__ == "__main__":
    initial_temperature = 1000
    cooling_rate = 0.95
    iter_per_temp = 100
    initial_solution = np.random.uniform(-10, 10)

    print("初始解:", initial_solution)

    optimized_solution = simulated_annealing(initial_temperature, cooling_rate, initial_solution, iter_per_temp)
    print("优化后的解:", optimized_solution)
