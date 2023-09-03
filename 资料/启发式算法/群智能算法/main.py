import numpy as np


# 目标函数
def target_function(x):
    return x ** 2


# 粒子群优化算法实现
def pso(n_particles, n_iterations, target_func, inertia, cognitive, social, bounds):
    # 初始化粒子位置和速度
    positions = np.random.uniform(bounds[0], bounds[1], n_particles)
    velocities = np.random.uniform(-1, 1, n_particles)

    # 初始化个体最优和全局最优位置
    personal_best_positions = np.copy(positions)
    personal_best_fitness = [target_func(p) for p in positions]
    global_best_position = personal_best_positions[np.argmin(personal_best_fitness)]
    global_best_fitness = min(personal_best_fitness)

    # 迭代粒子群
    for i in range(n_iterations):
        # 更新粒子速度和位置
        r1 = np.random.uniform(0, 1, n_particles)
        r2 = np.random.uniform(0, 1, n_particles)

        velocities = (inertia * velocities) \
                     + cognitive * r1 * (personal_best_positions - positions) \
                     + social * r2 * (global_best_position - positions)

        positions += velocities

        # 更新个体最优和全局最优位置
        for j in range(n_particles):
            current_fitness = target_func(positions[j])
            if current_fitness < personal_best_fitness[j]:
                personal_best_positions[j] = positions[j]
                personal_best_fitness[j] = current_fitness

                if current_fitness < global_best_fitness:
                    global_best_position = positions[j]
                    global_best_fitness = current_fitness

    return global_best_position, global_best_fitness


if __name__ == "__main__":
    n_particles = 30
    n_iterations = 100
    inertia = 0.7
    cognitive = 1.5
    social = 1.5
    bounds = (-10, 10)

    min_position, min_value = pso(n_particles, n_iterations, target_function, inertia, cognitive, social, bounds)

    print("最佳位置：", min_position)
    print("最小值：", min_value)
