import time, os
from reader import *
from euclidean import *

def test2():
    #import after accepting input or else GUI runs annoyingly
    from revision import lin
    import staticVars as sv
    from lkUtils import calculate, stringify, sleeper
    from genAlgos.rand import randomTour
    filepath = './tests/100.csv'

    #form GUI and weighted graph
    sv.cityNames, sv.rawCoords, sv.guiCoords = reader(filepath, sv.height, sv.width)
    sv.wg = weightedGraph(sv.rawCoords)

    #iterate through random tours
    bestCost = 999999999
    iterationList = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for iteration in iterationList:
        print("<<< {} iteration cap >>>".format(iteration))
        for i in range(iteration):
            print("-Running iteration {}".format(i))
            randTour, randCost = randomTour(sv.rawCoords, sv.cityNames, False)
            cost = lin(randTour, randCost, 1, 0, "test")
            print("--Iteration cost: {}".format(cost))
            if cost < bestCost:
                bestCost = cost
        print("-Best Cost: {}\n".format(bestCost)) 