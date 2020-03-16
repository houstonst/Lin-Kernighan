from tkinter import *
import staticVars as sv
from euclidean import *
from lkUtils import *

""" GRAPHICS """
def gui(tour, lines):
    #draw vertices
    for coord in sv.guiCoords:
      index = sv.guiCoords.index(coord)
      name = sv.cityNames[index]
      sv.wndw.create_oval((coord[0]-3, coord[1]-3, coord[0] + 3, coord[1] + 3), fill = "red")
      sv.wndw.create_text(coord[0], coord[1] - 12, fill = "black", font = "Times 10 bold", text = name)

    #draw edges
    lines = addLines(tour, lines, 1, "black")


""" STEPS TWO AND SEVEN"""
#find 5 longest edges in a tour not already added in
def longEdges(scanStart, added):
    flat_wg = []
    longest = []
    for i in range(len(sv.wg)):
        for j in range(len(sv.wg[i])):
            edge = (i, j)
            cost = sv.wg[i][j]
            flat_wg += [[edge, cost]]
    flat_wg.sort(key = lambda c:c[1], reverse = True)
    for [edge, cost] in flat_wg:
        if inTour(scanStart, edge) and not inSet(added, edge) and len(longest) < 5:
            longest += [edge]
    return longest
    
def removeEdge(nodeArray, edge, removed, lines, gainSum):
    #highlight node head and tail nodes
    nodeA = edge[0]
    nodeB = edge[1]
    nodeAx = sv.guiCoords[nodeA][0]
    nodeAy = sv.guiCoords[nodeA][1]
    nodeBx = sv.guiCoords[nodeB][0]
    nodeBy = sv.guiCoords[nodeB][1]
    sv.wndw.create_oval((nodeAx-3, nodeAy-3, nodeAx + 3, nodeAy + 3), fill = "blue")
    sv.wndw.create_oval((nodeBx-3, nodeBy-3, nodeBx + 3, nodeBy + 3), fill = "blue")

    #remove the edge
    print("-Pick an edge and remove it")
    path = []
    path = removeFromArray(nodeArray, edge)
    gainSum += sv.wg[edge[0]][edge[1]]
    removed.add(edge)
    sv.wndw.delete(lines[edge])
    print("--Removing {} produces path: {}".format(edge, stringify(path)))
    print("--Removed set contains: {}".format(removed))

    #calculate the gain-sum
    print("-Calculate the gain-sum")
    print("--Gain-sum = {}\n".format(gainSum))

    return path, nodeA, nodeB, removed, lines, gainSum


""" STEPS THREE AND EIGHT"""
def findCandidates(path, node, unused, removed):
    #unhighlight unused node
    unusedX = sv.guiCoords[unused][0]
    unusedY = sv.guiCoords[unused][1]
    sv.wndw.create_oval((unusedX-3, unusedY-3, unusedX + 3, unusedY + 3), fill = "red")

    #order 5 neighbors of the node by shortest to greatest distance
    print("-Order 5 neighbors of the node by shortest to greatest distance")
    candidates = []
    nodeSublist = sv.wg[node]
    prevNode, nextNode = around(path, node)
    for i in range(len(nodeSublist)):
        if i != path[0] and i != node and i != prevNode and i != nextNode and not inSet(removed, (node, i)): #checks if: recreating tour, self-directed, adjacent in path, already removed
            candidates += [[(node, i), nodeSublist[i]]]
    
    try: #candidates populated correctly
        candidates.sort(key = lambda c:c[1])
        candidates = candidates[:5]
        print("--Candidates: {}".format(stringify(candidates)))
    except: #no candidates exist
        print("--No existing candidates")

    return candidates

def addEdge(path, node, added, lines, gainSum, candidates, option):
    #check candidates against gain-sum and pick first edge that keeps it positive
    print("-Check 5 candidates against gain-sum and pick first edge that keeps it positive")
    edge = None
    for [candidateEdge, candidateCost] in candidates:
        if gainSum - candidateCost > 0:
            edge = candidateEdge
            break
    print("--Chosen edge: {}".format(edge))

    #add chosen edge
    print("-Add first edge to improve gain-sum")
    try:
        #highlight node
        nodeX = sv.guiCoords[node][0]
        nodeY = sv.guiCoords[node][1]
        sv.wndw.create_oval((nodeX-3, nodeY-3, nodeX + 3, nodeY + 3), fill = "red")

        #must reverse path if choosing other node in order to correctly generate delta path
        if option == 1:
            path = path.reverse()

        #create delta path
        deltaPath = path + [edge[1]]
        gainSum -= sv.wg[edge[0]][edge[1]]
        added.add(edge)
        a = sv.wndw.create_line(sv.guiCoords[edge[0]][0], sv.guiCoords[edge[0]][1], sv.guiCoords[edge[1]][0], sv.guiCoords[edge[1]][1], fill = "black")
        lines.update({edge: a})
        lines.update({(edge[1], edge[0]): a})
        print("--Adding {} produces delta path: {}".format(edge, stringify(deltaPath)))
        print("--Added set contains: {}".format(added))

        #calculate the gain-sum
        print("-Calculate the gain-sum")
        print("--Gain-sum = {}\n".format(gainSum))
    except:
        if option == 0: #tried first node. No feasible candidates existed
            print("\n-----------------------------------------------")
            print("\n<<< NO FEASIBLE CANDIDATES. TRY OTHER NODE. >>>")
        elif option == 1 or option == 2: #tried second node or could not create new delta path. Halt scan
            print("\n------------------------------------------")
            print("\n<<< NO FEASIBLE CANDIDATES. HALT SCAN. >>>")
        return [], path, added, lines, gainSum, True
    
    oldConfigs = [deltaPath, lines, gainSum]
    return oldConfigs, deltaPath, added, lines, gainSum, False


""" STEPS FIVE AND TEN """
def breakDelta(deltaPath, lines, gainSum, removed, red):
    #identify edge xw of the cycle incident with w that was not just added
    print("-Find edge xw of the cycle incident with w that was not just added")
    triNode = deltaPath[-1] #the node joining the tail and cycle
    x = deltaPath[deltaPath.index(triNode)+1] #x is the node in the adjacent edge that wasn't just added
    edge = (x, triNode)
    print("--Edge xw: {}".format(edge))

    #highlight node
    node = x #rename to make nodeX and nodeY names cleaner
    nodeX = sv.guiCoords[node][0]
    nodeY = sv.guiCoords[node][1]
    sv.wndw.create_oval((nodeX-3, nodeY-3, nodeX + 3, nodeY + 3), fill = "blue")

    #remove edge xw to create a path
    print("-Remove edge xw")
    path, edge = removeXW(deltaPath, triNode, edge)
    removed.add(edge)
    print("--Removing {} produces path: {}".format(edge, stringify(path))) #do not update removed. Only a check
    print("--Removed set contains: {}".format(removed))
    
    #update gain-sum and GUI
    print("-Update gain-sum and GUI")
    gainSum += sv.wg[edge[0]][edge[1]]
    if red == True:
        sv.wndw.itemconfig(lines[edge], fill = "red", dash = (5, 1))
    else:
        sv.wndw.delete(lines[edge])
    print("--Gain-sum = {}\n".format(gainSum))

    return path, gainSum, lines, removed

def generateTour(path, lines, gainSum):
    #join the two hanging ends of the path to form a tour
    print("-Join the two hanging ends of the path to form a tour")
    tour = path + [path[0]]
    edge = (tour[-2], tour[-1])

    #calculate the gain-sum
    print("-Calculate the gain-sum")
    gainSum -= sv.wg[edge[0]][edge[1]]
    print("--Gain-sum = {}\n".format(gainSum))

    #update GUI to reflect tour
    print("-Update gain-sum and GUI")
    a = sv.wndw.create_line(sv.guiCoords[edge[0]][0], sv.guiCoords[edge[0]][1], sv.guiCoords[edge[1]][0], sv.guiCoords[edge[1]][1], fill = "green")
    lines.update({edge: a})
    lines.update({(edge[1], edge[0]): a})
    print("--Adding {} produces tour: {}\n".format(edge, stringify(tour)))

    return tour, lines, gainSum


""" STEP SIX"""
def compareTour(tour, improved, best):
    #compare tour with best seen so far
    print("-Compare tour with the best seen so far. Replace as necessary")
    tourCost = calculate(tour)
    bestCost = calculate(best)
    if tourCost < bestCost:
        best = list(tour)
        improved = True
    print("--New tour cost: {}, old tour cost: {}".format(tourCost, bestCost))

    return best, improved

def restoreDelta(tour, oldConfigs):
    #oldConfigs = [deltaPath, lines, gainSum]

    #restore delta path
    print("-Restore delta path")
    deltaPath = oldConfigs[0]
    lines = oldConfigs[1]
    gainSum = oldConfigs[2]
    print("--Gain-sum: {}, delta path: {}".format(gainSum, stringify(deltaPath)))

    #restore GUI to continue scan
    print("-Restore GUI\n")
    triNode = deltaPath[-1] #the node joining the tail and cycle
    x = deltaPath[deltaPath.index(triNode)+1] #x is the node in the adjacent edge that wasn't just added
    edge = (x, triNode)
    removedEdge = (edge[1], edge[0])
    addedEdge = (tour[-2], tour[-1])
    sv.wndw.itemconfig(lines[removedEdge], fill = "black", dash = ())
    sv.wndw.delete(lines[addedEdge])

    return deltaPath, lines, gainSum


""" STEP 10 """
def concludeScan(scanStart, path, best, lines, bestLines):
    #reset nodeArray
    nodeArray = scanStart

    #reset added/removed sets
    print("-Reset added/removed sets")
    added = set()
    removed = set()
    print("--Added set: {}, removed set: {}".format(added, removed))

    #reset gain-sum
    print("-Reset gain-sum")
    gainSum = 0
    print("--Gain-sum: {}".format(gainSum))

    #reinitialize GUI
    print("-Reinitialize GUI\n")
    for line in lines.keys():
        sv.wndw.delete(lines[line])
    
    #draw best edges
    bestLines = addLines(best, bestLines, 4, "light blue")

    #overlap original edges
    lines = addLines(scanStart, lines, 1,  "black")

    return nodeArray, added, removed, lines, bestLines


""" STEP ELEVEN """
def prepareScan(scanStart, lines, bestLines):
    #clean GUI
    print("-Clean GUI\n")
    for line in lines.keys():
        sv.wndw.delete(lines[line])
    for line in bestLines.keys():
        sv.wndw.delete(bestLines[line])

    #draw original edges
    lines = addLines(scanStart, lines, 1, "black")
    
    return lines, bestLines