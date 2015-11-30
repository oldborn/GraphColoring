import random
from CSP import selecting
def backtrack_dfs(assignment, csp):
    var = selecting.pick_var(assignment, csp, 3)
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



def consistent(assignment, csp, i):
    # todo more advanced
    for n in range(len(csp[i].neighbors)):
        if assignment[i] == assignment[csp[i].neighbors[n]]:
            return False
    return True

def print_answer(assignment):
    print('%d\n%s' % (set(assignment).__len__(), ' '.join(map(str, assignment))))
    return

def backtrack_dfs_no_print(assignment, csp):
    var = selecting.pick_var(assignment, csp, 3)
    if var is None:
        # print_answer(assignment)
        return True
    for d in csp[var].domain:
        assignment[var] = d

        changed_domains = []
        for ni in range(csp[var].neighbors.__len__()):
            if d in csp[csp[var].neighbors[ni]].domain:
                csp[csp[var].neighbors[ni]].domain.remove(d)
                changed_domains.append(ni)

        if consistent(assignment, csp, var):
            if backtrack_dfs_no_print(assignment, csp):
                return True
        assignment[var] = -1

        for di in changed_domains:
            csp[di].domain.append(d)

    return False