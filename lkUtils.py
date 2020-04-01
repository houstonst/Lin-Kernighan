import staticVars as sv
import time

#find the node's adjacencies in a path or tour
def around(nodeArray, node):
    index = nodeArray.index(node)
    prevNode = -1
    nextNode = -1

    #tour (first and last node the same)
    if nodeArray[0] == nodeArray[-1]:
        if index == 0 or index == len(nodeArray)-1: #node at beginning or end
            prevNode = nodeArray[-2]
            nextNode = nodeArray[1]
        else: #node in middle
            prevNode = nodeArray[index-1]
            nextNode = nodeArray[index+1]

    
    #path (first and last not the same)
    else:
        if index > 0 and index < len(nodeArray)-1: #middle
            prevNode = nodeArray[index-1]
            nextNode = nodeArray[index+1]
        elif index == 0: #front
            prevNode = None
            nextNode = nodeArray[1]
        else: #end
            prevNode = nodeArray[-2]
            nextNode = None
    
    return prevNode, nextNode


#remove an edge from a tour
def removeUtil(nodeArray, edge):
    #destroy circuit
    path = nodeArray
    path.remove(path[0])
    
    #shift nodeArray until the edge is split between the beginning and end of the path
    while path[0] != edge[1] and path[-1] != edge[0]:
        val = path.pop()
        path.insert(0, val)

    return path


#print a path more concisely
def stringify(nodeArray):
    string = "["
    for node in nodeArray[:len(nodeArray)-1]:
        string += str(node) + ","
    string += str(nodeArray[-1]) + "]"
    return string


#see if an edge is in a tour or path
def inTour(nodeArray, edge):
    for i in range(len(nodeArray)-1):
        if nodeArray[i] == edge[0] and nodeArray[i+1] == edge[1]:
            return True
    return False


#calculate cost of path or tour
def calculate(nodeArray):
    cost = 0
    for i in range(len(nodeArray)-1):
        cost += sv.wg[nodeArray[i]][nodeArray[i+1]]
    return cost


#abstracts breakDelta()
def removeXW(deltaPath, triNode, edge):
    deltaPath = deltaPath[:-1] #remove last edge
    triNodeIndex = deltaPath.index(triNode)
    leftSection = deltaPath[:triNodeIndex+1] #left section goes until the triNode. Keep the same
    rightSection = deltaPath[triNodeIndex+1:]
    rightSection.reverse()
    edge = (edge[1], edge[0]) #reverse this data structure as well for GUI use
    path = leftSection + rightSection
    return path, edge


#check if edge or its reversal is in the set
def inSet(nodeSet, edge):
    if edge in nodeSet or (edge[1], edge[0]) in nodeSet:
        return True
    else:
        return False


#update the GUI with lines
def addLines(nodeArray, lines, width, color):
    for i in range(len(nodeArray)-1):
      node = nodeArray[i]
      nxt = nodeArray[i+1]
      a = sv.wndw.create_line(sv.guiCoords[node][0], sv.guiCoords[node][1], sv.guiCoords[nxt][0], sv.guiCoords[nxt][1], fill = color, width = width)
      lines.update({(node, nxt): a})
      lines.update({(nxt, node): a})

    return lines

#suspend execution
def sleeper(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print(0)