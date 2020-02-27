from lk import *
from lkUtils import *
from tkinter import *
from euclidean import *
from win32.win32api import GetSystemMetrics

""" GRAPHICS """
def gui(guiCoords, cityNames, tour, wndw, lines):
    #draw vertices
    for coord in guiCoords:
      index = guiCoords.index(coord)
      name = cityNames[index]
      wndw.create_oval((coord[0]-3, coord[1]-3, coord[0] + 3, coord[1] + 3), fill = "red")
      wndw.create_text(coord[0], coord[1] - 12, fill = "black", font = "Times 10 bold", text = name)

    #draw edges
    last = guiCoords[tour[len(tour)-1]]
    for i in range(len(tour)-1):
      node = tour[i]
      nxt = tour[i+1]
      a = wndw.create_line(guiCoords[node][0], guiCoords[node][1], guiCoords[nxt][0], guiCoords[nxt][1], fill = "black")
      lines.update({(node, nxt): a})
    a = wndw.create_line(guiCoords[tour[0]][0], guiCoords[tour[0]][1], last[0], last[1], fill = "black")


""" STEPS TWO AND SEVEN"""
def removeEdge(tour, node, added, removed, wndw, lines):
    #find the node's neighbors
    print("-Find the node's neighbors")
    prevNode, nextNode = around(tour, node)
    print("--Node: {}, Previous: {}, Next: {}".format(node, prevNode, nextNode))

    #pick an edge connecting the node to remove
    path = []
    print("-Pick an edge and remove it")
    prevEdge = (prevNode, node)
    nextEdge = (node, nextNode)
    for edge in [prevEdge, nextEdge]:
        if edge not in added:
            path = removeFromTour(tour, edge)
            removed.add(edge)
            wndw.delete(lines[edge])
            del lines[edge]
            break
    print("--Removing {} produces: {}".format(edge, stringify(path)))
    print("--Removed set contains: {}\n".format(removed))


""" STEPS THREE AND EIGHT"""
def addEdge():
    #order the neighbors of the node by distance
    print("-Order neighbors of the node by distance")
    print("--Stub")

    #check candidates against gain-sum
    print("-Check 5 candidates against gain-sum")
    print("--Stub")

    #add first edge to improve gain-sum
    print("-Add first edge to improve gain-sum")
    print("--Stub")

    #update GUI
    print("-Update GUI")
    print("--Stub\n")


""" STEPS FOUR AND NINE """
def formDelta():
    #this is a place-holder. Delta path formed by step 3
    print("-This is a place-holder. Delta path formed by steps 2+3, or 7+8\n")


""" STEPS FIVE AND TEN """
def generateTour():
    #remove edge xw of the cycle incident with w that was not just added
    print("-Remove edge xw of the cycle incident with w that was not just added")
    print("--Stub")


    #join the two hanging ends of the path to form a tour
    print("-Join the two hanging ends of the path to form a tour")
    print("--Stub")


    #update GUI to reflect tour
    print("-Update GUI")
    print("--Stub")


    #restore GUI to continue scan
    print("-Restore GUI")
    print("--Stub\n")


""" STEPS SIX AND TEN"""
def compareTour():
    #compare tour with best seen so far
    print("-Compare tour with the best seen so far. Replace as necessary")
    print("--Stub\n")