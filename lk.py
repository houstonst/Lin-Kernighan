from stepFuncs import *

def lin(rawCoords, guiCoords, cityNames, tour, cost, height, width, option):
    #rawCoords: The coordinates given in the input file
    #guiCoords: The coordinates after they are scaled for the GUI. For graphics only
    #cityNames: Array of unique identifiers for each node
    #tour: The tour resulting from Farthest Insertion. Stored as a list
    #cost: The summarized edge costs of tour
    #height: GUI height
    #width: GUI width
    #option: A "1" runs the heuristic with graphics, a "2" does so without
    
    """ INIT """
    #set GUI variables for all other functions to see
    height = GetSystemMetrics(1) - 200
    width = GetSystemMetrics(0) - 200
    root = Tk() #GUI for the starting path
    canvas_height = height
    canvas_width = width
    root.title("Lin-Kernighan")
    root.iconbitmap('./graphics/favicon.ico')
    wndw = Canvas(root, width = canvas_width, height = canvas_height)
    wndw.pack(expand = YES, fill=BOTH)
    lines = {}

    #draw onto GUI  
    print("<<< INITIALIZE GUI >>>\n")
    gui(guiCoords, cityNames, tour, wndw, lines)

    #store weighted graph
    wg = weightedGraph(rawCoords)

    #store added and removed edges
    added = set()
    removed = set()


    """ STEP TWO """
    def step2(): #non-callable function required for button functionality
        nonlocal lines
        print("<<< STEP 2 >>>")
        removeEdge(tour, 1, added, removed, wndw, lines) #needs parameter to specify where to remove from
        button.configure(text = "Add Edge", command = step3)


    """ STEP THREE """
    def step3():
        print("<<< STEP 3 >>>")
        addEdge() #needs parameter to specify where to add from
        button.configure(text = "Form Delta", command = step4)


    """ STEP FOUR """
    def step4():
        print("<<< STEP 4 >>>")
        formDelta() #placeholder. Delta formation already performed by steps 2 and 3
        button.configure(text = "Generate Tour", command = step5)


    """ STEP FIVE """
    def step5():
        print("<<< STEP 5 >>>")
        generateTour()
        button.configure(text = "Compare Tour", command = step6)
    

    """ STEP SIX """
    def step6():
        print("<<< STEP 6 >>>")
        compareTour()
        button.configure(text = "Remove Edge", command = step7)


    """ STEP SEVEN """
    def step7():
        print("<<< STEP 7 >>>")
        # removeEdge() #must remove xw
        button.configure(text = "Add Edge", command = step8)


    """ STEP EIGHT """
    def step8():
        print("<<< STEP 8 >>>")
        addEdge() #join x to nearby node y
        button.configure(text = "Form Delta", command = step9)


    """ STEP NINE """
    def step9():
        print("<<< STEP 9 >>>")
        formDelta() #placeholder. Delta formation already performed by steps 7 and 8
        button.configure(text = "Generate Tour", command = step10)


    """ STEP TEN """
    def step10():
        print("<<< STEP 10 >>>")
        generateTour()
        compareTour()
        # button.configure(text = "Remove Edge", command = step2)

    
    """ FINALIZE """
    #run GUI on loop
    button = Button(root, text = "Remove Edge", command = step2)
    button.pack(side = BOTTOM)
    root.mainloop()