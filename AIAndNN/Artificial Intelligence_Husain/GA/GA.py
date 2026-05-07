import random
import matplotlib.pyplot as plt
import numpy as np

# Genetic Algorithm Parameters
N = 8  # Number of queens
POPULATION_SIZE = 1000
MUTATION_RATE = 0.1
GENERATIONS = 1000

# Fitness function: Counts number of non-attacking queen pairs
def fitness(chromosome):
    non_attacking = 0
    for i in range(len(chromosome)):
        for j in range(i + 1, len(chromosome)):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking

# Create initial population of random chromosomes
def create_population():
    return [random.sample(range(N), N) for _ in range(POPULATION_SIZE)]

# Select top 50% individuals based on fitness
def selection(population):
    scores = [(fitness(ind), ind) for ind in population]
    scores.sort(reverse=True)
    return [ind for _, ind in scores[:POPULATION_SIZE // 2]]

# Crossover: combine parts of two parents to create a child
def crossover(parent1, parent2):
    idx = random.randint(1, N - 2)
    return parent1[:idx] + parent2[idx:]

# Mutation: randomly swap two positions
def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(N), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Main GA function
def genetic_algorithm():
    population = create_population()
    for generation in range(GENERATIONS):
        population = selection(population)
        new_population = population[:]
        while len(new_population) < POPULATION_SIZE:
            p1, p2 = random.sample(population, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
        best = max(population, key=fitness)
        if fitness(best) == 28:
            print(f"Solution found in generation {generation}")
            return best
    print(f"Best effort after max generations {generation}")
    return max(population, key=fitness)

# Visualize the solution on a black-and-white chessboard
def visualize_solution(solution):
    board_colors = np.zeros((N, N, 3))  # RGB image for color grid

    # Create black-and-white checkerboard pattern
    for i in range(N):
        for j in range(N):
            if (i + j) % 2 == 0:
                board_colors[i, j] = [1, 1, 1]  # white square
            else:
                board_colors[i, j] = [0, 0, 0]  # black square

    fig, ax = plt.subplots()
    ax.imshow(board_colors, extent=[0, N, 0, N])

    # Place red queen symbols
    for col, row in enumerate(solution):
        ax.text(col + 0.5, N - row - 0.5, '♛', fontsize=24, ha='center', va='center', color='red')

    # Clean up the axis
    ax.set_xticks(np.arange(N + 1))
    ax.set_yticks(np.arange(N + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_aspect('equal')
    ax.grid(False)
    plt.title("8-Queens on Chessboard")
    plt.show()


# Run the algorithm and visualize the result
if __name__ == "__main__":
    solution = genetic_algorithm()
    print("Solution:", solution)
    visualize_solution(solution)

