import read
import random
# from geneticalgorithm import doGA
from CSP import doCSP
# from geneticalgorithm import operations
import sys

if len(sys.argv) != 2:
        print("Usage: %s input_file" % sys.argv[0])
        sys.exit()

sys.setrecursionlimit(100000)


random.seed(12345678901)
nodes = read.read_problem(sys.argv[1])

# doGA.doGA(nodes)
doCSP.backtrack_search(nodes)




