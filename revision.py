import arr, copy, time
import staticVars as sv
from stepFuncs import *
from lkUtils import *
from loopFuncs import *

def lin(tour, cost, genTime, option):
    start = time.time()

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
    
    #print results
    print("LK Best Cost: {} units".format(round(retVal.cost)))
    end = time.time()
    runtime = end - start
    print("Lin-Kernighan runtime: {} sec".format(round(runtime)))
    print("Total runtime: {} sec\n".format(round(genTime + runtime)))
    trim = cost - retVal.cost
    print("<<< IMPROVEMENTS >>>")
    print("Trimmed: {} units".format(round(trim)))
    print("Reduced by: {}%".format(round(trim/cost*100)))

    #update GUI
    gui([], {})
    addLines(retVal.array, {}, 4, "light green")
    addLines(originalBest.array, {}, 1, "black")

    #loop GUI
    sv.root.mainloop()