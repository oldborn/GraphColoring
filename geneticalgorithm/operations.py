from CSP import doCSP
from geneticalgorithm.selection import tournament
from geneticalgorithm.crossover import union
import random


def init_population(population_size, nodes):
    ps = population_size
    population = [[-1 for x in range(nodes.__len__())] for i in range(ps)]
    for genome in population:
        doCSP.backtrack_search_with_assignment(nodes, genome)
    return population


def evaluate(population):
    evaluation = []
    for p in population:
        evaluation.append(fitness(p))
    return evaluation


def fitness(genome):
    return (set(genome)).__len__()


def select(evaluation, population, tournament_size):
    return tournament.selection(evaluation, population, tournament_size)


def get_elite(evaluation):
    print(min(evaluation))
    return evaluation.index(min(evaluation))


def cross_over_all(mating_pool, population):
    new_population = []
    while new_population.__len__() != population.__len__():
        i = random.randint(0, mating_pool.__len__() - 1)
        parent1_index = mating_pool.pop(i)
        i = random.randint(0, mating_pool.__len__() - 1)
        parent2_index = mating_pool.pop(i)
        parents = (population[parent1_index], population[parent2_index])
        children = cross_over(parents)
        new_population.append(children[0])
        new_population.append(children[1])
    return new_population

# expects (genome, genome), returns (childgenome, childgenome)
def cross_over(parents):
    return union.crossover(parents)

def fix_anomalies(population, nodes):
    domain = [x for x in range(nodes.__len__())]
    for p in population:
        for i in range(p.__len__()):
            neighbor_colors = [p[ni] for ni in nodes[i].neighbors]
            for n in nodes[i].neighbors:
                if p[i] == p[n]:
                    # print("not consistent")
                    #domain_diff = [c for c in domain if c not in [p[ni] for ni in nodes[i].neighbors] and domain_diff.__len__() == 0]
                    for c in domain:
                        if c not in neighbor_colors:
                            p[i] = c
                            break
                # else:
                #     print("consistent")
    return


