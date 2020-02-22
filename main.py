from win32.win32api import GetSystemMetrics
from reader import *
from fi import *

def main():
    #set window size
    height = GetSystemMetrics(1) - 200
    width = GetSystemMetrics(0) - 200

    #accept input
    print("Enter a .csv or .txt file [example.csv or example.txt]:")
    file = "./tests/" + input()

    #process input and run farthest insertion
    cityNames, rawCoords, guiCoords = reader(file, height, width)
    farthestInsertion(rawCoords, guiCoords, cityNames, height, width, "1")

if __name__ == "__main__":
    main()