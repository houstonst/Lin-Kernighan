import time, os
from reader import *
from euclidean import *

def test(solmax):
    #import after accepting input or else GUI runs annoyingly
    from revision import lin
    import staticVars as sv
    from fi import farthestInsertion
    from nn import nearestNeighbor
    from lkUtils import calculate, stringify, sleeper
    from rand import randomTour

    #iterate through files and run lin-kernighan
    files = ["6.csv", "11.csv", "14.csv", "26.csv", "29.csv", "48.csv", "52.csv", "76.csv", "100.csv", "105.csv", "107.csv", "120.csv", "152.txt", "195.csv", "200.txt", "225.txt", "299.txt", "318.txt", "439.txt", "575.txt"]
    algos = ["nearest", "farthest"]
    for i in range(len(files)):
        #cooldown
        if i == 4:
            sleeper(30)

        #execute
        print("<<< TESTING {} ON SOLMAX {} >>>".format(files[i], solmax))
        filepath = "./tests/" + files[i]
        for j in range(len(algos)):
            #data header
            print("{}:".format(algos[j]))

            #form GUI and weighted graph
            sv.cityNames, sv.rawCoords, sv.guiCoords = reader(filepath, sv.height, sv.width)
            sv.wg = weightedGraph(sv.rawCoords)

            #create initial tour
            start = time.time()
            tour = None
            cost = None
            if algos[j] == "farthest":
                tour, cost = farthestInsertion(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2", False)
            elif algos[j] == "nearest":
                tour, cost = nearestNeighbor(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2", False)
            else:
                tour, cost = randomTour(sv.rawCoords, sv.cityNames, False)

            #print tour info
            end = time.time()
            runtime = end - start

            #run lin-kernighan
            lin(tour, cost, solmax, runtime, "test")
        print("\n")
            

def solve(filepath, solmax):
    print("Pick a path generation algorithm (random by default):")
    print("""-farthest: Farthest Insertion
-nearest: Nearest Neighbor
-fixed: Fixed Tour defined in code\n""")
    algo = input()
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
    from revision import lin
    import staticVars as sv
    from fi import farthestInsertion
    from nn import nearestNeighbor
    from lkUtils import calculate, stringify
    from rand import randomTour

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
        tour = [5,3,13,8,10,1,11,9,12,2,7,0,6,4,5] #14
        cost = calculate(tour)
    else:
        tour, cost = randomTour(sv.rawCoords, sv.cityNames, False)
    
    #print tour info
    end = time.time()
    runtime = end - start
    print("Initial Cost: {} units".format(round(cost)))
    print("Tour generation runtime: {} sec\n".format(round(runtime)))

    #run lin-kernighan
    print("<<< RUN LIN-KERNIGHAN (SOLMAX = {})>>>".format(solmax))
    lin(tour, cost, solmax, runtime, option)

if __name__ == "__main__":
    #clear the console
    clear = lambda: os.system('cls')
    clear()

    #accept input
    print("Enter a .csv or .txt file [example.csv or example.txt]. Alternatively, enter 'test' in order to benchmark:\n")
    inp = input()
    clear()

    print("Choose a solmax:\n")
    solmax = input()
    clear()

    #run either the tests or problem solver
    if inp == "test":
        test(solmax)
        # clear()
    else:
        filepath = "./tests/" + inp
        solve(filepath, solmax)
        clear()

