import numpy as np


def fitness_function(solution):
    return np.sum(solution)


def generate_population(population_size, n_genes):
    return np.random.randint(0, 2, (population_size, n_genes))


def selection(population, fitness_scores, n_select):
    idx = np.argsort(fitness_scores)[-n_select:]
    return population[idx, :]


def crossover(parents, n_offspring):
    n_genes = parents.shape[1]
    offspring = np.zeros((n_offspring, n_genes))

    for i in range(n_offspring):
        r = np.random.choice(parents.shape[0], 2, replace=False)
        parent1, parent2 = parents[r, :]

        crossover_point = np.random.randint(0, n_genes)
        offspring[i, :crossover_point] = parent1[:crossover_point]
        offspring[i, crossover_point:] = parent2[crossover_point:]

    return offspring


def mutation(offspring, mutation_rate):
    for i in range(offspring.shape[0]):
        for j in range(offspring.shape[1]):
            if np.random.rand() < mutation_rate:
                offspring[i, j] = 1 - offspring[i, j]
    return offspring


def genetic_algorithm(generations, population_size, n_select, n_offspring, mutation_rate):
    n_genes = 10

    population = generate_population(population_size, n_genes)

    for generation in range(generations):
        fitness_scores = [fitness_function(solution) for solution in population]

        parents = selection(population, fitness_scores, n_select)

        offspring = crossover(parents, n_offspring)

        offspring = mutation(offspring, mutation_rate)

        population = np.vstack([parents, offspring])

    best_solution = population[np.argmax(fitness_scores), :]

    return best_solution


if __name__ == "__main__":
    generations = 100
    population_size = 50
    n_select = 20
    n_offspring = 30
    mutation_rate = 0.05

    optimized_solution = genetic_algorithm(generations, population_size, n_select, n_offspring, mutation_rate)
    print("最优解：", optimized_solution)
    print("最大适应值：", fitness_function(optimized_solution))
