import staticVars as sv
from stepFuncs import *

def lin(tour, cost):
    #tour: The tour resulting from Farthest Insertion. Stored as a list
    #cost: The summarized edge costs of tour
    
    """ STORE DYNAMIC VARIABLES """
    #line IDs
    lines = {}

    #draw onto GUI  
    print("<<< INITIALIZE GUI >>>\n")
    gui(tour, lines)

    #edge sets
    added = set()
    removed = set()

    #path or tour
    nodeArray = []

    #node of interest
    node = None

    #gain-sum
    gainSum = 0


    """ STEP TWO """
    def step2():
        nonlocal nodeArray, node, removed, gainSum #declare nonlocal if overwriting variables in scope of lin()
        print("<<< STEP 2 >>>")

        #list the 5 longest edges in descending order
        print("-List the 5 longest edges in tour")
        longest = longEdges(tour, added)        
        print("--Longest: {}".format(stringify(longest)))

        #remove edges
        nodeArray, node, removed, gainSum = removeEdge(tour, longest[0], removed, lines, gainSum)

        #update button
        button.configure(text = "Add Edge", command = step3)


    """ STEP THREE """
    def step3():
        print("<<< STEP 3 >>>")
        #find 5 candidates
        candidates = findCandidates(nodeArray, node, removed) #needs parameter to specify where to add from

        #add a candidate edge
        addEdge(nodeArray, node, added, lines, gainSum, candidates)

        #update button
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

        #update button
        button.configure(text = "Compare Tour", command = step6)
    

    """ STEP SIX """
    def step6():
        print("<<< STEP 6 >>>")
        compareTour()

        #update button
        button.configure(text = "Remove Edge", command = step7)


    """ STEP SEVEN """
    def step7():
        print("<<< STEP 7 >>>")
        # removeEdge() #must remove xw

        #update button
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

        #update button
        button.configure(text = "Generate Tour", command = step10)


    """ STEP TEN """
    def step10():
        print("<<< STEP 10 >>>")
        generateTour()
        compareTour()

        #update button
        # button.configure(text = "Remove Edge", command = step2)

    
    """ FINALIZE """
    #run GUI on loop
    button = Button(sv.root, text = "Remove Edge", command = step2, relief = RIDGE, bd = 4)
    button.pack(side = BOTTOM, pady = 15)
    sv.root.mainloop()
