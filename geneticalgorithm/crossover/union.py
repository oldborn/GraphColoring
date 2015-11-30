import random
def crossover(parents):
    child1 = []
    child2 = []
    parent1 = parents[0]
    parent2 = parents[1]
    for i in range(parents[0].__len__()):
        randint = random.randint(0, 1)
        if randint == 0:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])
    return child1, child2
