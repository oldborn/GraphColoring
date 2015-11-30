import random


def selection(evaluation, population, tournament_size):
    mating_pool = []
    while mating_pool.__len__() < population.__len__():
        mating_pool.append(tournament(evaluation, population, tournament_size))
    return mating_pool


def tournament(evaluation, population, ts, ):
    tournament_pool = [random.randint(0, population.__len__() - 1) for i in range(ts)]
    tournament_evaluation = [evaluation[i] for i in tournament_pool]
    min_index = tournament_evaluation.index(min(tournament_evaluation))
    return tournament_pool[min_index]
