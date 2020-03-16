from reader import *
from euclidean import *
from rand import *

def main():
    #accept input
    print("Enter a .csv or .txt file [example.csv or example.txt]:")
    file = "./tests/" + input()

    #import after accepting input or else GUI runs annoyingly
    from lk import lin
    import staticVars as sv
    from fi import farthestInsertion
    from lkUtils import calculate

    #form GUI and weighted graph
    sv.cityNames, sv.rawCoords, sv.guiCoords = reader(file, sv.height, sv.width)
    sv.wg = weightedGraph(sv.rawCoords)

    #create initial tour
    tour, cost = farthestInsertion(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2") #farthestInsertion
    # tour, cost = randomTour(sv.rawCoords, sv.cityNames) #random tour

    # tour = [3,0,2,5,1,4,3] #fixed tour for 6.csv
    # cost = calculate(tour)
    
    #run lin-kernighan
    lin(tour, cost)

if __name__ == "__main__":
    main()