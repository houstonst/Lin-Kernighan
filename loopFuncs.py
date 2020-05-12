from lkUtils import *
from stepFuncs import *
import copy

def sweep(best, solmax):
    for i in range(len(best.array)-1):
        edge = (best.array[i], best.array[i+1])
        improved = scan(best, edge, solmax)
        if improved:
            return best
    return False

def expand(best, verts, bFactor, index, reverse):
    resultingVerts = []
    for vert in verts:
        node = vert.array[index]
        candidates = findCandidates(vert, bFactor, node)
        for candidate in candidates:
            try:
                newVert = copy.deepcopy(vert)
                checkedTour, checkedCost = deltaOps(newVert, candidate, reverse)
                if checkedCost < best.cost:
                    best.array = checkedTour
                    best.cost = checkedCost
                else:
                    pass
                resultingVerts += [newVert]
            except:
                pass

    return resultingVerts

def scan(best, edge, solmax):
    improved = False
    scanOriginalBest = copy.deepcopy(best)
    level1vert = removeEdge(copy.deepcopy(best), edge)

    #scan from head
    level2headVerts = expand(best, [level1vert], solmax, -1, False)
    level3headVerts = expand(best, level2headVerts, solmax, -1, False)
    levelNheadVerts = expand(best, level3headVerts, 1, -1, False)
    i = 5
    while len(levelNheadVerts) > 0: #a path still exists that we can expand
        levelNheadVerts = expand(best, levelNheadVerts, 1, -1, False)
        i += 1

    if best.cost < scanOriginalBest.cost:
        improved = True

    else:
        #scan from tail
        level2tailVerts = expand(best, [level1vert], solmax, 0, True)
        level3tailVerts = expand(best, level2tailVerts, solmax, -1, False)
        levelNtailVerts = expand(best, level3tailVerts, 1, -1, False)
        i = 5
        while len(levelNtailVerts) > 0: #a path still exists that we can expand
            levelNtailVerts = expand(best, levelNtailVerts, 1, -1, False)
            i += 1

        if best.cost < scanOriginalBest.cost:
            improved = True

    return improved