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

    #form GUI and weighted graph
    sv.cityNames, sv.rawCoords, sv.guiCoords = reader(file, sv.height, sv.width)
    sv.wg = weightedGraph(sv.rawCoords)

    #create initial tour
    # tour, cost = farthestInsertion(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2") #farthestInsertion
    # tour, cost = randomTour(sv.rawCoords, sv.cityNames) #random tour
    tour = [9,4,10,6,8,1,3,5,2,0,7,9] #fixed tour based on 11.csv
    cost = 0
    for i in range(len(tour)-1):
      cost += sv.wg[tour[i]][tour[i+1]]
    
    #run lin-kernighan
    lin(tour, cost)

if __name__ == "__main__":
    main()
