def pick_var(assignment, csp):
    indexes = [x for x in range(assignment.__len__()) if assignment[x] == -1]
    # todo more advanced
    # this part is most neighbored node -> better than random
    # if indexes.__len__() > 0:
    #     max_restriction = [csp[i].neighbors.__len__() for i in indexes]
    #     index_of_max = max_restriction.index(max(max_restriction))
    #     return indexes[index_of_max]

    # random selection bad results
    # if indexes.__len__() > 0:
    #     return random.choice(indexes)

    # let's try minimum domain -> it gave 20 from 5th instance 14 from others
    if indexes.__len__() > 0:
            min_domain = [csp[i].domain.__len__() for i in indexes]
            index_of_min = min_domain.index(min(min_domain))
            return indexes[index_of_min]


    return None

def pick_var_RD(assignment, csp):
    # max(max_restrict/domain)
    indexes = [x for x in range(assignment.__len__()) if assignment[x] == -1]
    max_restriction = []
    if indexes.__len__() > 0:
        max_restriction = [csp[i].neighbors.__len__() for i in indexes]
    min_domain = []
    if indexes.__len__() > 0:
        min_domain = [csp[i].domain.__len__() for i in indexes]
    if max_restriction.__len__() > 0 and min_domain.__len__() > 0:
        rd_list = [max_restriction[i]/min_domain[i] for i in range(max_restriction.__len__())]
        index_of_max = rd_list.index(max(rd_list))
        return indexes[index_of_max]

    return None

def pick_var_minimum_domain_max_restrict(assignment, csp):
    # not bad but, second returns 6... although 5th returns 20 :)
    indexes = [x for x in range(assignment.__len__()) if assignment[x] == -1]
    if indexes.__len__() > 0:
        min_domain = [csp[i].domain.__len__() for i in indexes]
        indexes_of_min = [i for i in range(min_domain.__len__()) if min(min_domain) == min_domain[i]]
        max_of_min = [csp[i].neighbors.__len__() for i in indexes_of_min]
        index = max_of_min.index(max(max_of_min))
        index = indexes_of_min[index]
        return indexes[index]

    return None

