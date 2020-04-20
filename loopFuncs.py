from lkUtils import *
from stepFuncs import *
import copy

def sweep(best, solmax):
    # print("<<<< Sweep with tour: {}, cost: {} >>>>".format(stringify(best.array), best.cost))
    for i in range(len(best.array)-1):
        edge = (best.array[i], best.array[i+1])
        # print("\n<<< Scan {} >>>".format(i))
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
                    # print("REPLACEMENT!")
                    # print("Previous best tour: {}, cost: {}".format(stringify(best.array), best.cost))
                    best.array = checkedTour
                    best.cost = checkedCost
                    # print("New best tour: {}, cost: {}\n".format(best.array, best.cost))
                else:
                    # print("ATTEMPTED. NO REPLACEMENT.\n")
                    pass
                resultingVerts += [newVert]
            except:
                # print("Edge {} is an infeasible candidate".format(candidate[0]))
                # print("NO ATTEMPT. CEASE WORK ON VERT.\n")
                pass

    return resultingVerts

def scan(best, edge, solmax):
    improved = False
    scanOriginalBest = copy.deepcopy(best)
    # print("-Scanning after removing edge {}\n".format(edge))
    level1vert = removeEdge(copy.deepcopy(best), edge)

    #scan from head
    # print("<< Head level 2 >>")
    level2headVerts = expand(best, [level1vert], solmax, -1, False)
    # print("<< Head level 3 >>")
    level3headVerts = expand(best, level2headVerts, solmax, -1, False)
    # print("<< Head level 4 >>")
    levelNheadVerts = expand(best, level3headVerts, 1, -1, False)
    i = 5
    # print("<< Head level {} >>".format(i))
    while len(levelNheadVerts) > 0: #a path still exists that we can expand
        levelNheadVerts = expand(best, levelNheadVerts, 1, -1, False)
        i += 1
    # print("<< HEAD COMPLETE >>")

    if best.cost < scanOriginalBest.cost:
        improved = True

    else:
        #scan from tail
        # print("\n<< Tail level 2 >>")
        level2tailVerts = expand(best, [level1vert], solmax, 0, True)
        # print("< Tail level 3 >")
        level3tailVerts = expand(best, level2tailVerts, solmax, -1, False)
        # print("< Tail level 4 >")
        levelNtailVerts = expand(best, level3tailVerts, 1, -1, False)
        i = 5
        # print("< Tail level {} >".format(i))
        while len(levelNtailVerts) > 0: #a path still exists that we can expand
            levelNtailVerts = expand(best, levelNtailVerts, 1, -1, False)
            i += 1
        # print("<< TAIL COMPLETE >>\n")

        if best.cost < scanOriginalBest.cost:
            improved = True

    return improved