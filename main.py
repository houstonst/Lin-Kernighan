from reader import *
from euclidean import *

def main():
    #accept input and run farthest insertion
    print("Enter a .csv or .txt file [example.csv or example.txt]:")
    file = "./tests/" + input()

    #import after accepting input or else GUI runs annoyingly
    from lk import lin
    import staticVars as sv
    from fi import farthestInsertion

    sv.cityNames, sv.rawCoords, sv.guiCoords = reader(file, sv.height, sv.width)
    sv.wg = weightedGraph(sv.rawCoords)
    fiTour, fiCost = farthestInsertion(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2") #1: GUI; 2: STDOUT
    
    #run lin-kernighan
    lin(fiTour, fiCost)

if __name__ == "__main__":
    main()
