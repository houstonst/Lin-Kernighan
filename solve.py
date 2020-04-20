import time, os
from reader import *
from euclidean import *
from tkinter import *

def solve():
    #clear the console
    clear = lambda: os.system('cls')
    clear()
    
    #accept input
    print("Enter a .csv or .txt file [example.csv or example.txt]:\n")
    inp = input()
    filepath = "./tests/" + inp
    clear()

    print("Pick a path generation algorithm (random by default):")
    print("""-farthest: Farthest Insertion
-nearest: Nearest Neighbor
-fixed: Fixed Tour defined in code\n""")
    algo = input()
    clear()

    print("Choose a solmax:\n")
    rawsol = input()
    solmax = int(rawsol)
    clear()

#     print("Pick to run in step mode, at pace, or fast as possible:")
#     print("""-step
# -slow
# -medium
# -fast
# -max"\n"")
    # option = input()
    # clear()
    option = "step"

    #import after accepting input or else GUI runs annoyingly
    from lk import lin
    import staticVars as sv
    from genAlgos.fi import farthestInsertion
    from genAlgos.nn import nearestNeighbor
    from lkUtils import calculate, stringify
    from genAlgos.rand import randomTour

    #form GUI and weighted graph
    sv.cityNames, sv.rawCoords, sv.guiCoords = reader(filepath, sv.height, sv.width)
    sv.wg = weightedGraph(sv.rawCoords)

    #create initial tour
    start = time.time()
    tour = None
    cost = None
    if algo == "farthest":
        tour, cost = farthestInsertion(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2", False)
    elif algo == "nearest":
        tour, cost = nearestNeighbor(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2", False)
    elif algo == "fixed":
        tour = [0,5,42,24,10,45,35,4,26,2,29,34,41,16,22,3,23,14,25,13,11,12,15,40,9,1,8,38,31,44,18,7,28,6,37,19,27,17,43,30,36,46,33,20,47,21,32,39,0]
        cost = calculate(tour)
    else:
        tour, cost = randomTour(sv.rawCoords, sv.cityNames, False)
    
    #print tour info
    end = time.time()
    runtime = end - start

    #run gui
    root = Tk()
    root.title("Lin-Kernighan")
    root.iconbitmap('./graphics/favicon.ico')
    wndw = Canvas(root, width = sv.width, height = sv.height)
    wndw.pack(expand = YES, fill=BOTH)

    #run lin-kernighan
    print("<<< RUNNING LIN-KERNIGHAN ON PROBLEM {} >>>".format(inp))
    lin(tour, cost, solmax, runtime, option, root, wndw)