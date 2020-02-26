from tkinter import *
from euclidean import *
from win32.win32api import GetSystemMetrics


""" GRAPHICS """
def gui():
    print("-Stub\n")
    
    # height = GetSystemMetrics(1) - 200
    # width = GetSystemMetrics(0) - 200
    # root = Tk() #GUI for the starting path
    # canvas_height = height
    # canvas_width = width
    # root.title("Lin-Kernighan")
    # root.iconbitmap('./graphics/favicon.ico')
    # wndw = Canvas(root, width = canvas_width, height = canvas_height)
    # wndw.pack(expand = YES, fill=BOTH)
    # for coord in guiCoords:
    #   index = guiCoords.index(coord)
    #   name = cityNames[index]
    #   wndw.create_oval((coord[0]-3, coord[1]-3, coord[0] + 3, coord[1] + 3), fill = "red")
    #   wndw.create_text(coord[0], coord[1] - 12, fill = "black", font = "Times 10 bold", text = name)

""" STEPS TWO AND SEVEN"""
def removeEdge():
    #tour: The nodes stored as an array. An edge exists between two adjacent nodes. Ex.) [0, 4, 2, 1, 3, 0]
    #weightedGraph: 2D matrix where the value at the intersection between a row and column indicates that edge's cost

    #pick an edge to remove
    print("-Pick an edge to remove")
    print("--Stub")

    #pick one of its ends, v
    print("-Pick one of its ends to be joined elsewhere")
    print("--Stub")

    #update GUI
    print("-Update GUI")
    print("--Stub\n")

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