import arr, copy
import staticVars as sv
from stepFuncs import *
from lkUtils import *
from loopFuncs import *

def lin(tour, cost, option):
    """
    #while improvedTour != None:
        #improvedTour = sweep(tour)
    #return bestTour #improvedTour not found, lin-kernighan complete
    """
    #store best tour seen across entire LK heuristic
    best = arr.Tour(tour, cost)
    originalBest = copy.deepcopy(best)

    #begin sweep on the best tour
    retVal = None
    while True:
        best = sweep(best)
        if best == False:
            break
        else:
            retVal = best
    print("Original tour: {}, cost: {}".format(stringify(originalBest.array), originalBest.cost))
    print("LK best tour: {}, cost: {}".format(stringify(retVal.array), retVal.cost))

    gui([], {})
    addLines(retVal.array, {}, 4, "light green")
    addLines(originalBest.array, {}, 1, "black")

    sv.root.mainloop()