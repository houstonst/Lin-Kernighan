import staticVars as sv
from stepFuncs import *
from copy import deepcopy

def lin(tour, cost):
    #tour: The tour resulting from Farthest Insertion. Stored as a list
    #cost: The summarized edge costs of tour
    
    """ STORE DYNAMIC VARIABLES """
    #store starting tour as variable for node/edge scan initiation
    orig = list(tour)

    #iteration tracker
    i = 0

    #best tour
    best = list(tour) #prevents pointer issue

    #improved boolean
    improved = False

    #track old configurations
    oldConfigs = []

    #line IDs
    lines = {}
    bestLines = {}

    #draw onto GUI  
    print("<<< INITIALIZE GUI >>>\n")
    gui(tour, lines)

    #edge sets
    added = set()
    removed = set()

    #working path or tour
    nodeArray = []

    #node of interest
    nodeA = None
    nodeB = None

    #gain-sum
    gainSum = 0


    """ STEP TWO """
    def step2():
        nonlocal i, nodeArray, nodeA, nodeB, removed, lines, bestLines, gainSum #declare nonlocal if overwriting variables in scope of lin()
        if i < 5:
            print("<<< STEP 2 >>>")
            nodeArray = list(best)

            #list the 5 longest edges in descending order
            print("-List the 5 longest edges in tour")
            longest = longEdges(nodeArray, added)        
            print("--Longest: {}".format(stringify(longest)))

            #remove edges
            nodeArray, nodeA, nodeB, removed, lines, gainSum = removeEdge(nodeArray, longest[i], removed, lines, gainSum)

            #update button
            button.configure(text = "Add Edge", command = step3)
        else:
            print("{ SWEEP COMPLETE. HALT WORK. }")
            print("-BEST TOUR IN SWEEP: {}".format(stringify(best)))
            print("--ORIGINAL COST: {}".format(calculate(orig)))
            print("--BEST TOUR COST: {}\n\n\n".format(calculate(best)))

            #update GUI
            for line in lines.keys():
                sv.wndw.delete(lines[line])
            bestLines = addLines(best, bestLines, 4, "light green")
            lines = addLines(orig, lines, 1, "black")

            #configure button
            button.configure(text = "Done", command = None)


    """ STEP THREE """
    def step3():
        nonlocal i, oldConfigs, nodeArray, added, lines, gainSum, improved
        print("<<< STEP 3 >>>")
        #find 5 candidates and add edge if possible
        candidates = findCandidates(nodeArray, nodeA, nodeB, removed)
        oldConfigs, nodeArray, added, lines, gainSum, complete = addEdge(nodeArray, nodeA, added, lines, gainSum, candidates, 0)

        #try other node if previous attempt unsuccessful
        if complete == True:
            candidates = findCandidates(nodeArray, nodeB, nodeA, removed)
            oldConfigs, nodeArray, added, lines, gainSum, complete = addEdge(nodeArray, nodeB, added, lines, gainSum, candidates, 1)

        #check for completion and improvement
        if complete and improved: #scan complete, improvement made. Cease sweep and restart heuristic
            print("-NEW BEST TOUR: {}\n".format(stringify(best)))
            i = 0
            button.configure(text = "Show Difference", command = step10)
        elif complete and not improved:#scan complete, no improvement made. Continue sweep with new scan
            print("-UNCHANGED BEST TOUR: {}\n".format(stringify(best)))
            i += 1
            button.configure(text = "Show Difference", command = step10)
        else: #scan incomplete, continue scan
            button.configure(text = "Break Delta", command = step5a)


    """ STEP FIVEa """
    def step5a():
        nonlocal nodeArray, gainSum, lines, removed
        print("<<< STEP 5a >>>")
        nodeArray, gainSum, lines, removed = breakDelta(nodeArray, lines, gainSum, removed, True)

        #update button
        button.configure(text = "Visualize Tour", command = step5b)


    """ STEP FIVEb """
    def step5b():
        nonlocal nodeArray, lines, gainSum
        print("<<< STEP 5b >>>")
        nodeArray, lines, gainSum = generateTour(nodeArray, lines, gainSum)

        #update button
        button.configure(text = "Compare Tour", command = step6a)
    

    """ STEP SIXa """
    def step6a():
        nonlocal best, improved
        print("<<< STEP 6a >>>")
        best, improved = compareTour(nodeArray, improved, best)
        print("--Best tour: {}\n".format(stringify(best)))
        #update button
        button.configure(text = "Restore Delta", command = step6b)

    """ STEP SIXb """
    def step6b():
        nonlocal nodeArray, lines, gainSum
        print("<<< STEP 6b >>>")
        nodeArray, lines, gainSum = restoreDelta(nodeArray, oldConfigs)

        #update button
        button.configure(text = "Break Delta", command = step7)


    """ STEP SEVEN """
    def step7():
        nonlocal nodeArray, gainSum, lines, removed
        print("<<< STEP 7 >>>")
        nodeArray, gainSum, lines, removed = breakDelta(nodeArray, lines, gainSum, removed, False)

        #update button
        button.configure(text = "Add Edge", command = step8)


    """ STEP EIGHT """
    def step8():
        nonlocal oldConfigs, nodeArray, added, lines, gainSum, i, orig, improved
        print("<<< STEP 8 >>>")
        #specify last node
        nodeA = nodeArray[-1]
        nodeB = nodeArray[0] #arbitrary. Not applied in step 8 so doesn't matter
        
        #find candidates
        candidates = findCandidates(nodeArray, nodeA, nodeB, removed)

        #add a candidate edge
        oldConfigs, nodeArray, added, lines, gainSum, complete = addEdge(nodeArray, nodeA, added, lines, gainSum, candidates, 2)

        #check for completion and improvement
        if complete and improved: #scan complete, improvement made. Cease sweep and restart heuristic
            print("-NEW BEST TOUR: {}\n".format(stringify(best)))
            i = 0
            button.configure(text = "Show Difference", command = step10)
        elif complete and not improved:#scan complete, no improvement made. Continue sweep with new scan
            print("-UNCHANGED BEST TOUR: {}\n".format(stringify(best)))
            i += 1
            button.configure(text = "Show Difference", command = step10)
        else: #scan incomplete, continue scan
            button.configure(text = "Break Delta", command = step5a)


    """ STEP TEN """
    def step10():
        nonlocal orig, nodeArray, added, removed, lines, bestLines
        print("<<< STEP 10 >>>")
        
        #prepare for next node/edge scan
        nodeArray, added, removed, lines, bestLines = concludeScan(orig, nodeArray, best, lines, bestLines)

        #configure button
        button.configure(text = "Sweep GUI", command = step11)

    def step11():
        nonlocal orig, lines, bestLines, improved
        print("<<< STEP 11 >>>")
        #sweep GUI
        lines, bestLines = prepareScan(best, lines, bestLines)

        #set orig and improved to prepare for a new scan
        orig = list(best)
        improved = False

        #configure button
        button.configure(text = "Begin Scan", command = step2)

    
    """ FINALIZE """
    #run GUI on loop
    button = Button(sv.root, text = "Remove Edge", command = step2, relief = RIDGE, bd = 4)
    button.pack(side = BOTTOM, pady = 15)
    sv.root.mainloop()