import staticVars as sv

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
def removeFromTour(tour, edge):
    #destroy circuit
    path = tour
    path.remove(path[0])
    
    #shift tour until the edge is split between the beginning and end of the path
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