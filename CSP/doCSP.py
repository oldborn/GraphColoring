from CSP import operations

def backtrack_search(csp):
    domain = [x for x in range(csp.__len__())]
    for n in csp:
        n.domain = list(domain)
    return operations.backtrack_dfs([-1 for x in range(csp.__len__())], csp)