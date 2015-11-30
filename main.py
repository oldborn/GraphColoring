import read
import random
from CSP import doCSP
from geneticalgorithm import doGA
import sys

# if len(sys.argv) != 2:
#         print("Usage: %s input_file" % sys.argv[0])
#         sys.exit()

sys.setrecursionlimit(100000)


random.seed(12345673331)
# nodes = read.read_problem(sys.argv[1])
nodes = read.read_problem("data/gc_250_7")
doGA.doGA(nodes)
doCSP.backtrack_search(nodes)




