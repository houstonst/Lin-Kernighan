import staticVars as sv
from stepFuncs import *
from lkUtils import *

#def extend(path, candidate):
    #form delta path
    #check tour
    #break delta path
    #find closest candidate
    #return candidates


#def scan(edge): #level0
    #remove edge
    #for head, tail in edge: #level1 nodes
        #find 5 candidates
        #for each candidate: #level2 nodes
            #form delta path
            #check resulting tour
            #break delta path
            #find 5 candidates
            #for each candidate: #level3 nodes
                #form delta path
                #check tour
                #break delta path
                #find closest candidate #level4->N nodes
                #while(candidateExists): 
                    #closestCandidate = extend(path, candidate)
                #completed level4->N
            #completed level3
        #completed level2
    #completed level1
#completed level0

"""-------------------------------------------------------------"""
class Vert:
    def __init__(self, path, added, removed, gainSum):
        self.path = path
        self.added = added
        self.removed = removed
        self.gainSum = gainSum

class Tour:
    def __init__(self, cycle, cost):
        self.cycle = cycle
        self.cost = cost
    def info(self):
        print("Tour: {}, Cost: {}".format(stringify(self.cycle), self.cost))

# def sweep(tour):
#     """
#     for i in range(len(tour-1)):
#         edge = (tour[i], tour[i+1])
#         #newTour = scan(edge)
#         #if newTour != oldTour:
#             #return newTour
#         #else:
#             #continue
#     #return None #no newTour returned, so no improvement made and sweep complete
#     """
#     pass

# def expand(list of verts, branchFactor):
#     """
#     #resulting verts = []
#     #for vert in list of verts
#         #find {branchFactor} candidates for the last node in the vert.path
#         #for each candidate in candidates:
#             #form delta path
#             #check tour
#             #break delta path and create vert with updated path, added/removed sets, and gainSum
#             #add vert to list of resulting verts
#     #return resulting verts
#     """
#     pass

# def scan2(edge):
    """
    #level1vert = remove edge (from level 0 tour)
    #for end in edge:
        #level2verts = expand(level1vert, 5)
        #level3verts = expand(level2verts, 5)
        #levelNverts = expand(level3verts, 1)
        #while levelNverts > 0: #a path still exists that we can expand
            #levelNverts = expand(levelNverts, 1)
    #return best tour
    """
    pass

def lin(tour, cost, option):
    """
    #while improvedTour != None:
        #improvedTour = sweep(tour)
    #return bestTour #improvedTour not found, lin-kernighan complete
    """
    best = Tour(tour, cost)
    best.info()
