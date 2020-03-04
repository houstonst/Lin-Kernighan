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
    last = sv.guiCoords[tour[len(tour)-1]]
    for i in range(len(tour)-1):
      node = tour[i]
      nxt = tour[i+1]
      a = sv.wndw.create_line(sv.guiCoords[node][0], sv.guiCoords[node][1], sv.guiCoords[nxt][0], sv.guiCoords[nxt][1], fill = "black")
      lines.update({(node, nxt): a})
      lines.update({(nxt, node): a})
    a = sv.wndw.create_line(sv.guiCoords[tour[0]][0], sv.guiCoords[tour[0]][1], last[0], last[1], fill = "black")


""" STEPS TWO AND SEVEN"""
#find 5 longest edges in a tour not already added in
def longEdges(tour, added):
    flat_wg = []
    longest = []
    for i in range(len(sv.wg)):
        for j in range(len(sv.wg[i])):
            edge = (i, j)
            cost = sv.wg[i][j]
            flat_wg += [[edge, cost]]
    flat_wg.sort(key = lambda c:c[1], reverse = True)
    for [edge, cost] in flat_wg:
        if inTour(tour, edge) and not inSet(added, edge) and len(longest) < 5:
            longest += [edge]
    return longest
    
def removeEdge(nodeArray, edge, removed, lines, gainSum):
    #highlight node
    node = edge[0]
    nodeX = sv.guiCoords[node][0]
    nodeY = sv.guiCoords[node][1]
    sv.wndw.create_oval((nodeX-3, nodeY-3, nodeX + 3, nodeY + 3), fill = "blue")

    #pick an edge connecting the node to remove
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

    return path, node, removed, lines, gainSum


""" STEPS THREE AND EIGHT"""
def findCandidates(path, node, removed):
    #order 5 neighbors of the node by shortest to greatest distance
    print("-Order 5 neighbors of the node by shortest to greatest distance")
    candidates = []
    nodeSublist = sv.wg[node]
    prevNode, nextNode = around(path, node)
    for i in range(len(nodeSublist)):
        if i != path[0] and i != node and i != prevNode and i != nextNode and not inSet(removed, (node, i)): #checks if: recreating tour, self-directed, adjacent in path, already removed
            candidates += [[(node, i), nodeSublist[i]]]
    
    try:
        candidates.sort(key = lambda c:c[1])
        candidates = candidates[:5]
        print("--Candidates: {}".format(stringify(candidates)))
    except:
        print("--Candidates: {}".format(candidates))

    return candidates

def addEdge(path, node, added, lines, gainSum, candidates):
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
        print("\n-------------------------------------------------------")
        print("\n{ NO FEASIBLE CANDIDATES. HALT SCAN. RETURN BEST TOUR }\n")
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
def compareTour(tour, best):
    #compare tour with best seen so far
    print("-Compare tour with the best seen so far. Replace as necessary")
    tourCost = calculate(tour)
    bestCost = calculate(best)
    if tourCost < bestCost:
        best = list(tour)
    print("--New tour cost: {}, old tour cost: {}".format(tourCost, bestCost))

    return best

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
def concludeScan(orig, path, best, lines):
    #print orig
    print("-Original path: {}".format(stringify(orig)))

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
    print("-Reinitialize GUI")
    for line in lines:
        sv.wndw.delete(lines[line])
    
    #draw best edges
    last = sv.guiCoords[best[len(best)-1]]
    for i in range(len(best)-1):
      node = best[i]
      nxt = best[i+1]
      a = sv.wndw.create_line(sv.guiCoords[node][0], sv.guiCoords[node][1], sv.guiCoords[nxt][0], sv.guiCoords[nxt][1], fill = "light blue", width = 4)
    a = sv.wndw.create_line(sv.guiCoords[best[0]][0], sv.guiCoords[best[0]][1], last[0], last[1], fill = "light blue", width = 4)

    #overlap original edges
    last = sv.guiCoords[orig[len(orig)-1]]
    for i in range(len(orig)-1):
      node = orig[i]
      nxt = orig[i+1]
      a = sv.wndw.create_line(sv.guiCoords[node][0], sv.guiCoords[node][1], sv.guiCoords[nxt][0], sv.guiCoords[nxt][1], fill = "black")
    a = sv.wndw.create_line(sv.guiCoords[orig[0]][0], sv.guiCoords[orig[0]][1], last[0], last[1], fill = "black")

    return orig, added, removed


""" STEP ELEVEN """
def prepareScan(orig, lines):
    #sweep GUI
    print("-Sweep GUI")
    for line in lines:
        sv.wndw.delete(lines[line])

    #overlap original edges
    last = sv.guiCoords[orig[len(orig)-1]]
    for i in range(len(orig)-1):
      node = orig[i]
      nxt = orig[i+1]
      a = sv.wndw.create_line(sv.guiCoords[node][0], sv.guiCoords[node][1], sv.guiCoords[nxt][0], sv.guiCoords[nxt][1], fill = "black")
    a = sv.wndw.create_line(sv.guiCoords[orig[0]][0], sv.guiCoords[orig[0]][1], last[0], last[1], fill = "black")
