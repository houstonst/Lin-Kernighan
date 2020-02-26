from lkUtils import *

def lin(rawCoords, guiCoords, cityNames, tour, cost, height, width, guiLines, option):
    #rawCoords: The coordinates given in the input file
    #guiCoords: The coordinates after they are scaled for the GUI. For graphics only
    #cityNames: Array of unique identifiers for each node
    #tour: The tour resulting from Farthest Insertion. Stored as a list
    #cost: The summarized edge costs of tour
    #height: GUI height
    #width: GUI width
    #guiLines: List of graphical edges from Farthest Insertion. Used to update GUI
    #option: A "1" runs the heuristic with graphics, a "2" does so without
    
    """ INIT """
    #initialize GUI
    print("<<< INITIALIZE GUI >>>")
    gui()

    #store weighted graph
    wg = weightedGraph(rawCoords)

    """ STEP TWO """
    print("<<< STEP 2 >>>")
    removeEdge() #needs parameter to specify where to remove from
    
    """ STEP THREE """
    print("<<< STEP 3 >>>")
    addEdge() #needs parameter to specify where to add from

    """ STEP FOUR """
    print("<<< STEP 4 >>>")
    formDelta() #placeholder. Delta formation already performed by steps 2 and 3

    """ STEP FIVE """
    print("<<< STEP 5 >>>")
    generateTour()

    """ STEP SIX """
    print("<<< STEP 6 >>>")
    compareTour()

    """ STEP SEVEN """
    print("<<< STEP 7 >>>")
    removeEdge() #must remove xw

    """ STEP EIGHT """
    print("<<< STEP 8 >>>")
    addEdge() #join x to nearby node y

    """ STEP NINE """
    print("<<< STEP 9 >>>")
    formDelta() #placeholder. Delta formation already performed by steps 7 and 8

    """ STEP TEN """
    print("<<< STEP 10 >>>")
    generateTour()
    compareTour()
