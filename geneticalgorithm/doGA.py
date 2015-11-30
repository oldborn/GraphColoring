from geneticalgorithm import operations
import random
import datetime
from CSP import doCSP
def doGA(nodes):
    ts = 5
    is_elite = True
    max_iteration_count = 100
    max_non_improve_iteration = 20
    improvement = []
    # assignment = [-1 for x in range(nodes.__len__())]
    # doCSP.backtrack_search_with_assignment(nodes, assignment)
    # print(assignment)
    # todo-in-review create first population
    t1 = datetime.datetime.now()
    population = operations.init_population(10, nodes)
    for t in range(max_iteration_count):
        # todo-in-review evaluate
        t2 = datetime.datetime.now()
        evaluation = operations.evaluate(population)
        # todo-in-review selection
        t3 = datetime.datetime.now()
        matingpool = operations.select(evaluation, population, ts)
        # todo-in-review cross-over
        t4 = datetime.datetime.now()
        new_population = operations.cross_over_all(matingpool, population)
        # todo mutation
        t5 = datetime.datetime.now()
        # todo-in-review fix
        t6 = datetime.datetime.now()
        operations.fix_anomalies(new_population, nodes)
        # todo-in-review add elite
        t7 = datetime.datetime.now()
        new_population.pop(random.randint(0, new_population.__len__() - 1))
        new_population.append(population[operations.get_elite(evaluation)])
        population = new_population

        if min(evaluation) in improvement:
            improvement.append(min(evaluation))
        else:
            improvement.clear()
            improvement.append(min(evaluation))
        if improvement.__len__() > max_non_improve_iteration:
            break
    return