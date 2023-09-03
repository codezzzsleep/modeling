import numpy as np


def target_function(x):
    return x ** 2


def create_initial_population(population_size, min_value, max_value):
    return np.random.uniform(min_value, max_value, population_size)


def selection(population, fitness_values, n_select):
    selected_indices = np.argsort(fitness_values)[:n_select]
    return population[selected_indices]


def crossover(parents, n_offspring):
    offspring = np.empty(n_offspring)
    crossover_points = np.random.randint(0, parents.shape[1], n_offspring)

    for i in range(n_offspring):
        parent1_idx = i % parents.shape[0]
        parent2_idx = (i + 1) % parents.shape[0]
        crossover_point = crossover_points[i]

        offspring[i] = np.hstack((parents[parent1_idx][:crossover_point], parents[parent2_idx][crossover_point:]))

    return offspring


def mutation(population, mutation_rate, min_value, max_value):
    for i in range(population.shape[0]):
        if np.random.rand() < mutation_rate:
            population[i] *= np.random.uniform(min_value, max_value)
    return population


def genetic_algorithm(generations, population_size, n_select, n_offspring, mutation_rate, min_value=-10, max_value=10):
    population = create_initial_population(population_size, min_value, max_value)

    for _ in range(generations):
        fitness_values = target_function(population)

        parents = selection(population, fitness_values, n_select)
        offspring = crossover(parents, n_offspring)

        offspring_mutated = mutation(offspring, mutation_rate, min_value, max_value)
        population = np.hstack((parents, offspring_mutated))

    best_solution_index = np.argmin(target_function(population))
    return population[best_solution_index]


if __name__ == "__main__":
    generations = 100
    population_size = 50
    n_select = 20
    n_offspring = 30
    mutation_rate = 0.2

    optimized_solution = genetic_algorithm(generations, population_size, n_select, n_offspring, mutation_rate)
    print("优化后的解:", optimized_solution)
