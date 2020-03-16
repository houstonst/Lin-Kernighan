import staticVars as sv
from stepFuncs import *
from copy import deepcopy

def lin(tour, cost):
    #tour: The tour resulting from Farthest Insertion. Stored as a list
    #cost: The summarized edge costs of tour
    
    """ STORE DYNAMIC VARIABLES """
    #store very first tour
    start = list(tour)

    #store starting tour for each scan
    scanStart = list(tour)

    #step iteration tracker
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
        nonlocal i, nodeArray, nodeA, nodeB, removed, lines, bestLines, gainSum
        if i < 5:
            print("<<< STEP 2 >>>")
            nodeArray = list(best) #a new scan works with the best tour seen so far

            #list the 5 longest edges that haven't already been added in descending order
            print("-List the 5 longest edges in tour")
            longest = longEdges(nodeArray, added)        
            print("--Longest edges: {}".format(stringify(longest)))

            #remove edges
            nodeArray, nodeA, nodeB, removed, lines, gainSum = removeEdge(nodeArray, longest[i], removed, lines, gainSum)

            #advance to next step
            button.configure(text = "Add Edge", command = step3)
            # step3()

        else:
            #scans complete, sweeps complete, heuristic finished. Print final results
            startCost = round(calculate(start))
            bestCost = round(calculate(best))
            print("<<< LIN-KERNIGHAN COMPLETE. HALT WORK. >>>")
            print("-BEST TOUR: {}".format(stringify(best)))
            print("--ORIGINAL TOUR COST: {}".format(startCost))
            print("--BEST TOUR COST: {}".format(bestCost))
            division = bestCost / startCost
            decimal = 1 - division
            print("--IMPROVED BY {}%\n\n\n".format(round(decimal*100)))

            #update GUI
            for line in lines.keys():
                sv.wndw.delete(lines[line])
            bestLines = addLines(best, bestLines, 4, "light green")
            lines = addLines(start, lines, 1, "black")

            #delete button
            button.pack_forget()


    """ STEP THREE """
    def step3():
        nonlocal i, oldConfigs, nodeArray, added, lines, gainSum, improved
        print("<<< STEP 3 >>>")

        #find 5 candidates and add edge if possible
        candidates = findCandidates(nodeArray, nodeA, nodeB, removed)
        oldConfigs, nodeArray, added, lines, gainSum, complete = addEdge(nodeArray, nodeA, added, lines, gainSum, candidates, 0)

        #try other node if previous attempt unsuccessful (could not find feasible nodeA candidates)
        if complete:
            candidates = findCandidates(nodeArray, nodeB, nodeA, removed)
            oldConfigs, nodeArray, added, lines, gainSum, complete = addEdge(nodeArray, nodeB, added, lines, gainSum, candidates, 1)

        #check for completion and improvement
        if complete and improved: #scan complete, improvement made. Cease sweep and restart heuristic with best tour
            print("-NEW BEST TOUR: {}\n".format(stringify(best)))
            i = 0
            button.configure(text = "Show Difference", command = step10)
            # step10()
        elif complete and not improved:#scan complete, no improvement made. Continue sweep with new scan
            print("-UNCHANGED BEST TOUR: {}\n".format(stringify(best)))
            i += 1
            button.configure(text = "Show Difference", command = step10)
            # step10()
        else: #scan incomplete, continue scan
            button.configure(text = "Break Delta", command = step5a)
            # step5a()


    """ STEP FIVEa """
    def step5a():
        nonlocal nodeArray, gainSum, lines, removed
        print("<<< STEP 5a >>>")

        #break the delta path in order to check the tour
        nodeArray, gainSum, lines, removed = breakDelta(nodeArray, lines, gainSum, removed, True)

        #advance to next step
        button.configure(text = "Visualize Tour", command = step5b)
        # step5b()


    """ STEP FIVEb """
    def step5b():
        nonlocal nodeArray, lines, gainSum
        print("<<< STEP 5b >>>")

        #visualize the tour
        nodeArray, lines, gainSum = generateTour(nodeArray, lines, gainSum)

        #advance to next step
        button.configure(text = "Compare Tour", command = step6a)
        # step6a()


    """ STEP SIXa """
    def step6a():
        nonlocal best, improved
        print("<<< STEP 6a >>>")

        #compare the generated tour with the previously known best
        best, improved = compareTour(nodeArray, improved, best)
        print("--Best tour: {}\n".format(stringify(best)))

        #advance to next step
        button.configure(text = "Restore Delta", command = step6b)
        # step6b()


    """ STEP SIXb """
    def step6b():
        nonlocal nodeArray, lines, gainSum
        print("<<< STEP 6b >>>")

        #restore the old configurations (i.e. return to the delta path)
        nodeArray, lines, gainSum = restoreDelta(nodeArray, oldConfigs)

        #advance to next step
        button.configure(text = "Break Delta", command = step7)
        # step7()


    """ STEP SEVEN """
    def step7():
        nonlocal nodeArray, gainSum, lines, removed
        print("<<< STEP 7 >>>")

        #break the delta again, this time to create a different delta
        nodeArray, gainSum, lines, removed = breakDelta(nodeArray, lines, gainSum, removed, False)

        #advance to next step
        button.configure(text = "Add Edge", command = step8)
        # step8()


    """ STEP EIGHT """
    def step8():
        nonlocal oldConfigs, nodeArray, added, lines, gainSum, i, scanStart, improved
        print("<<< STEP 8 >>>")

        #define the head and tail nodes of the tour
        nodeA = nodeArray[-1]
        nodeB = nodeArray[0] #arbitrary. Not applied in step 8 so doesn't matter
        
        #find candidates
        candidates = findCandidates(nodeArray, nodeA, nodeB, removed)

        #add a candidate edge
        oldConfigs, nodeArray, added, lines, gainSum, complete = addEdge(nodeArray, nodeA, added, lines, gainSum, candidates, 2)

        #check for completion and improvement
        if complete and improved: #scan complete, improvement made. Cease sweep and restart heuristic with best known tour
            print("-NEW BEST TOUR: {}\n".format(stringify(best)))
            i = 0
            button.configure(text = "Show Difference", command = step10)
            # step10()
        elif complete and not improved:#scan complete, no improvement made. Continue sweep with new scan
            print("-UNCHANGED BEST TOUR: {}\n".format(stringify(best)))
            i += 1
            button.configure(text = "Show Difference", command = step10)
            # step10()
        else: #scan incomplete, continue scan
            button.configure(text = "Break Delta", command = step5a)
            # step5a()


    """ STEP TEN """
    def step10():
        nonlocal scanStart, nodeArray, added, removed, lines, bestLines
        print("<<< STEP 10 >>>")
        
        #prepare for next node/edge scan
        nodeArray, added, removed, lines, bestLines = concludeScan(scanStart, nodeArray, best, lines, bestLines)

        #configure button
        button.configure(text = "Clean GUI", command = step11)
        # step11()


    """ STEP ELEVEN """
    def step11():
        nonlocal scanStart, lines, bestLines, improved
        print("<<< STEP 11 >>>")
        
        #clean GUI
        lines, bestLines = prepareScan(best, lines, bestLines)

        #set scan starting tour and improved to prepare for a new scan
        scanStart = list(best)
        improved = False

        #configure button
        button.configure(text = "Begin Scan", command = step2)
        # step2()

    
    """ GUI LOOP """
    #run GUI on loop
    button = Button(sv.root, text = "Remove Edge", command = step2, relief = RIDGE, bd = 4)
    button.pack(side = BOTTOM, pady = 15)
    sv.root.mainloop()