import random

# tournament selection
def selection(population):
    # todo add elitism
    mating_pool = []
    while mating_pool.__len__() != population.__len__():
        competitors = [random.choice(population) for x in range(int(population.__len__() / 10))]
        fitness_list = [set(competitors[index]).__len__() for index in range(competitors.__len__())]
        champion = competitors[fitness_list.index(max(fitness_list))]
        mating_pool.append(champion)
    return mating_pool


def create_population(population_size, n_items):
    population = []
    for i in range(population_size):
        population.append([random.randint(0, n_items) for n in range(n_items)])
    return population


def fix_population(population, map):
    # print(population[1])
    # print(get_colors_of_neighbors(map, population[1], 1))
    all_colors = [x for x in range(map.__len__())]
    for chromosome in population:
        for index in range(chromosome.__len__()):
            color = chromosome[index]
            neighbor_colors = get_colors_of_neighbors(map, chromosome, index)
            mn = map[index].neighbors
            if neighbor_colors.__contains__(color):
                # print(neighbor_colors.__contains__(color))
                color = random.choice([x for x in all_colors if x not in neighbor_colors])
                chromosome[index] = color
                # print(neighbor_colors.__contains__(color))
    print("---------------------------------")
    return population


def get_colors_of_neighbors(map, chromosome, index):
    neighbors = map[index].neighbors
    colors = []
    # colors = [chromosome[n] for n in neighbors if not colors.__contains__(chromosome[n])]
    # set([chromosome[n] for n in neighbors])
    for n in neighbors:
        if not colors.__contains__(chromosome[n]):
            colors.append(chromosome[n])
    return colors

def fitness(chromosome):
    return set(chromosome).__len__()

