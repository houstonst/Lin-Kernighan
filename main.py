from reader import *
from euclidean import *

def main():
    #accept input
    print("-Enter a .csv or .txt file [example.csv or example.txt]:")
    file = "./tests/" + input()

    print("\n-Pick a path generation algorithm (random by default):")
    print("""--farthest: Farthest Insertion
--nearest: Nearest Neighbor
--fixed: Fixed Tour defined in code""")
    algo = input()

    print("\n-Pick to run in step mode, at pace, or fast as possible:")
    print("""--step
--slow
--medium
--fast
--max""")
    option = input()
    print("\n")

    #import after accepting input or else GUI runs annoyingly
    from lk import lin
    import staticVars as sv
    from fi import farthestInsertion
    from nn import nearestNeighbor
    from lkUtils import calculate
    from rand import randomTour

    #form GUI and weighted graph
    sv.cityNames, sv.rawCoords, sv.guiCoords = reader(file, sv.height, sv.width)
    sv.wg = weightedGraph(sv.rawCoords)

    #create initial tour
    tour = None
    cost = None
    if algo == "farthest":
        tour, cost = farthestInsertion(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2")
    elif algo == "nearest":
        tour, cost = nearestNeighbor(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2")
    elif algo == "fixed":
        tour = [3,0,2,5,1,4,3] #fixed tour for 6.csv
        cost = calculate(tour)
        print("-Initial Cost: {}".format(cost))
        print("-Initial Tour: {}\n".format(stringify(tour)))
    else:
        tour, cost = randomTour(sv.rawCoords, sv.cityNames)

    #run lin-kernighan
    lin(tour, cost, option)

if __name__ == "__main__":
    main()