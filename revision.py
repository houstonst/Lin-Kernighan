import arr, copy, time
import staticVars as sv
from stepRev import *
from lkUtils import *
from loopFuncs import *

def lin(tour, genCost, solmax, genTime, option):
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
    if option != "test1" and option != "test2":
        #Print Data
        print("LK Best Cost: {} units".format(round(retVal.cost)))
        print("Lin-Kernighan runtime: {} sec".format(round(runtime)))
        print("Total runtime: {} sec\n".format(round(genTime + runtime)))
        print("<<< IMPROVEMENTS >>>")
        print("Trimmed: {} units".format(round(trim)))
        print("Reduced by: {}%".format(round(trim/genCost*100)))
        
        #GUI
        gui([], {})
        addLines(retVal.array, {}, 4, "light green")
        addLines(originalBest.array, {}, 1, "black")
        sv.root.mainloop()
    
    else:
        print("-- genCost: {} units | lkCost: {} units | genTime: {} sec | lkTime: {} sec | totTime: {} sec | imp: {}%".format(
            round(genCost, 2),
            round(retVal.cost, 2),
            round(genTime, 2),
            round(runtime, 2),
            round(genTime + runtime, 2),
            round(trim/genCost*100, 2)
        ))