from fi import *
from lk import lin
from reader import *
from win32.win32api import GetSystemMetrics

def main():
    #set GUI parameters
    height = GetSystemMetrics(1) - 200
    width = GetSystemMetrics(0) - 200

    #accept input and run farthest insertion
    print("Enter a .csv or .txt file [example.csv or example.txt]:")
    file = "./tests/" + input()
    cityNames, rawCoords, guiCoords = reader(file, height, width)
    fiTour, fiCost, guiLines = farthestInsertion(rawCoords, guiCoords, cityNames, height, width, "2") #1: GUI; 2: STDOUT
    
    #run lin-kernighan
    lin(rawCoords, guiCoords, cityNames, fiTour, fiCost, guiLines, height, width, "1") #1: GUI; 2: STDOUT

if __name__ == "__main__":
    main()