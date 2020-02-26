from fi import *
from lk import lin
from reader import *
from win32.win32api import GetSystemMetrics


def main():
    #set window size
    height = GetSystemMetrics(1) - 200
    width = GetSystemMetrics(0) - 200

    #accept input
    print("Enter a .csv or .txt file [example.csv or example.txt]:")
    file = "./tests/" + input()

    #process input and run farthest insertion. Store farthest insertion tour and cost into variables
    cityNames, rawCoords, guiCoords = reader(file, height, width)
    fiTour, fiCost = farthestInsertion(rawCoords, guiCoords, cityNames, height, width, "2") #1: GUI; 2: STDOUT
    print("\n---- Farthest Insertion complete ----\n")
    
    #run lin-kernighan on farthest insertion tour and cost
    lin(rawCoords, guiCoords, cityNames, fiTour, fiCost, height, width, "1") #1: GUI; 2: STDOUT

if __name__ == "__main__":
    main()
