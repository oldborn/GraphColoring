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

    # todo max(max_restrict/domain)

    return None