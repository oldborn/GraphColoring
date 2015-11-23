class Node:
    def __init__(self):
        self.neighbors = []
        self.domain = []

    def __repr__(self):
        return self.neighbors.__repr__()

    @staticmethod
    def construct():
        return Node()


def read_problem(file_name):
    lines = open(file_name).readlines()

    tokens = lines[0].split()
    n_items = int(tokens[0])
    n_edges = int(tokens[1])
    nodes = [Node() for n in range(n_items)]
    for line in lines[1: n_edges + 1]:
        tokens = line.split()
        first = int(tokens[0])
        second = int(tokens[1])
        nodes[first].neighbors.append(second)
        nodes[second].neighbors.append(first)
    return nodes
