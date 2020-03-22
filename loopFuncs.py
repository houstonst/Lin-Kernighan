from lkUtils import *
from stepRev import *
import copy

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

"""--------------------------DEPRECATED------------------------------"""

def sweep(best):
    print("<<<< Sweep with tour: {}, cost: {} >>>>".format(stringify(best.array), best.cost))
    for i in range(len(best.array)-1):
        edge = (best.array[i], best.array[i+1])
        print("\n<<< Scan {} >>>".format(i))
        improved = scan(best, edge)
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
                    print("REPLACEMENT!")
                    print("Previous best tour: {}, cost: {}".format(stringify(best.array), best.cost))
                    best.array = checkedTour
                    best.cost = checkedCost
                    print("New best tour: {}, cost: {}\n".format(best.array, best.cost))
                else:
                    print("ATTEMPTED. NO REPLACEMENT.\n")
                resultingVerts += [newVert]
            except:
                print("Edge {} is an infeasible candidate".format(candidate[0]))
                print("NO ATTEMPT. CEASE WORK ON VERT.\n")

    return resultingVerts

def scan(best, edge):
    improved = False
    scanOriginalBest = copy.deepcopy(best)
    print("-Scanning after removing edge {}\n".format(edge))
    level1vert = removeEdge(copy.deepcopy(best), edge)

    #scan from head
    print("<< Head level 2 >>")
    level2headVerts = expand(best, [level1vert], 5, -1, False)
    print("<< Head level 3 >>")
    level3headVerts = expand(best, level2headVerts, 5, -1, False)
    print("<< Head level 4 >>")
    levelNheadVerts = expand(best, level3headVerts, 1, -1, False)
    i = 5
    print("<< Head level {} >>".format(i))
    while len(levelNheadVerts) > 0: #a path still exists that we can expand
        levelNheadVerts = expand(best, levelNheadVerts, 1, -1, False)
        i += 1
    print("<< HEAD COMPLETE >>")

    scanOriginalBest.info()
    best.info()
    if best.cost < scanOriginalBest.cost:
        improved = True

    else:
        #scan from tail
        print("\n<< Tail level 2 >>")
        level2tailVerts = expand(best, [level1vert], 5, 0, True)
        print("< Tail level 3 >")
        level3tailVerts = expand(best, level2tailVerts, 5, -1, False)
        print("< Tail level 4 >")
        levelNtailVerts = expand(best, level3tailVerts, 1, -1, False)
        i = 5
        print("< Tail level {} >".format(i))
        while len(levelNtailVerts) > 0: #a path still exists that we can expand
            levelNtailVerts = expand(best, levelNtailVerts, 1, -1, False)
            i += 1
        print("<< TAIL COMPLETE >>\n")

        if best.cost < scanOriginalBest.cost:
            improved = True

    return improved