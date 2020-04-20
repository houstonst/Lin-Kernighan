import time, os
from reader import *
from euclidean import *

def randTest():
    #clear the console
    clear = lambda: os.system('cls')
    clear()
    
    #accept input
    print("Enter a .csv or .txt file [example.csv or example.txt]:\n")
    inp = input()
    filepath = "./tests/" + inp
    clear()

    print("Enter maximum number of random tours to improve:\n")
    rawCap = input()
    cap = int(rawCap)
    clear()

    print("Enter increment value for number of random tours to improve:\n")
    rawInc = input()
    inc = int(rawInc)
    clear()

    print("Choose a solmax:\n")
    rawsol = input()
    solmax = int(rawsol)
    clear()

    #import after accepting input or else GUI runs annoyingly
    from lk import lin
    import staticVars as sv
    from lkUtils import calculate, stringify, sleeper
    from genAlgos.rand import randomTour

    #form GUI and weighted graph
    sv.cityNames, sv.rawCoords, sv.guiCoords = reader(filepath, sv.height, sv.width)
    sv.wg = weightedGraph(sv.rawCoords)

    #iterate through random tours
    bestCost = 999999999
    iterationList = [i for i in range(1, cap+1, inc)]
    for iteration in iterationList:
        print("<<< {} RANDOM TOUR(S) >>>".format(iteration))
        for i in range(iteration):
            print("-running iteration {}".format(i+1))
            randTour, randCost = randomTour(sv.rawCoords, sv.cityNames, False)
            cost = lin(randTour, randCost, solmax, 0, "test2", None, None)
            if cost < bestCost:
                bestCost = cost
        print("-best cost: {}\n".format(bestCost)) 