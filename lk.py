import arr, copy, time
import staticVars as sv
from stepFuncs import *
from lkUtils import *
from loopFuncs import *

def lin(tour, genCost, solmax, genTime, option, root, wndw):
    start = time.time()

    #store best tour seen across entire LK heuristic
    best = arr.Tour(tour, genCost)
    originalBest = copy.deepcopy(best)

    #begin sweep on the best tour
    retVal = best
    while True:
        best = sweep(best, solmax)
        if best == False:
            break
        else:
            retVal = best
    
    #print results
    end = time.time()
    runtime = end - start
    trim = genCost - retVal.cost
    print("""--generation cost: {} units
--generation runtime: {} sec
--heuristic cost: {} units
--heuristic runtime: {} sec
--total time: {} sec
--improvement: {}%
""".format(
        round(genCost, 2),
        round(genTime, 2),
        round(retVal.cost, 2),
        round(runtime, 2),
        round(genTime + runtime, 2),
        round(trim/genCost*100, 2)
    ))

    #GUI
    if option != "test1" and option != "test2":
        gui([], {}, wndw)
        addLines(retVal.array, {}, 4, "light green", wndw)
        addLines(originalBest.array, {}, 1, "black", wndw)
        root.mainloop()

    return round(retVal.cost, 2)