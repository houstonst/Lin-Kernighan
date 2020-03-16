from lkUtils import stringify
import random
from euclidean import *

def randomTour(graph, nameArray):
  print("\n<<< GENERATE RANDOM TOUR >>>")
  path = []
  cost = 0.0
  wg = weightedGraph(graph)
  nodes = []

  for i in range(0, len(graph)):
    nodes.append(i)
  
  for i in range(0, len(graph)):
    randNode = random.choice(nodes)
    path.append(randNode)
    nodes.remove(randNode)
  
  path.append(path[0])

  for i in range(0, len(path)-1):
    cost += wg[path[i]][path[i+1]]

  print("-Initial Cost: {}".format(cost))
  print("-Initial Tour: {}\n".format(stringify(path)))

  return path, cost