import random

def backtrack_dfs(assignment, csp):
    var = pick_var(assignment, csp)
    if var is None:
        print_answer(assignment)
        return True
    for d in csp[var].domain:
        assignment[var] = d

        changed_domains = []
        for ni in range(csp[var].neighbors.__len__()):
            if d in csp[csp[var].neighbors[ni]].domain:
                csp[csp[var].neighbors[ni]].domain.remove(d)
                changed_domains.append(ni)

        if consistent(assignment, csp, var):
            if backtrack_dfs(assignment, csp):
                return True
        assignment[var] = -1

        for di in changed_domains:
            csp[di].domain.append(d)

    return False

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

def consistent(assignment, csp, i):
    # todo more advanced
    for n in range(len(csp[i].neighbors)):
        if assignment[i] == assignment[csp[i].neighbors[n]]:
            return False
    return True

def print_answer(assignment):
    print('%d\n%s' % (set(assignment).__len__(), ' '.join(map(str, assignment))))
    return