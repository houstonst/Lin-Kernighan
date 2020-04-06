import time, os
from reader import *
from euclidean import *

def test1():
    #import after accepting input or else GUI runs annoyingly
    from revision import lin
    import staticVars as sv
    from genAlgos.fi import farthestInsertion
    from genAlgos.nn import nearestNeighbor
    from lkUtils import calculate, stringify, sleeper
    from genAlgos.rand import randomTour

    #iterate through files and run lin-kernighan
    files = ["6.csv", "11.csv", "14.csv", "26.csv", "29.csv", "48.csv", "52.csv", "76.csv", "100.csv", "105.csv", "107.csv", "120.csv", "152.txt", "195.csv", "200.txt", "225.txt", "299.txt", "318.txt", "439.txt", "575.txt"]
    algos = ["nearest", "farthest"]
    for solmax in range (1, 10, 2):
        for j in range(len(files)):
            #cooldown
            if j > 6:
                # seconds = i**2
                # sleeper(seconds)
                pass

            #execute
            print("<<< TESTING {} ON SOLMAX {} >>>".format(files[j], solmax))
            filepath = "./tests/" + files[j]
            for k in range(len(algos)):
                #data header
                print("{}:".format(algos[k]))

                #form GUI and weighted graph
                sv.cityNames, sv.rawCoords, sv.guiCoords = reader(filepath, sv.height, sv.width)
                sv.wg = weightedGraph(sv.rawCoords)

                #create initial tour
                start = time.time()
                tour = None
                cost = None
                if algos[k] == "farthest" and files[j] == '575.txt':
                    tour = [23,22,21,44,20,43,19,42,41,18,17,16,40,39,15,14,12,13,35,58,36,59,82,60,37,38,61,62,63,64,86,83,84,85,110,109,131,108,107,129,106,81,104,105,128,130,153,152,151,150,149,127,148,126,125,124,123,101,103,102,80,79,78,77,76,100,99,98,75,97,96,74,73,51,50,28,29,52,53,31,54,55,32,56,57,33,34,11,10,9,7,8,30,6,4,5,27,26,3,2,1,25,24,47,48,49,72,70,71,93,94,95,117,116,139,141,118,119,120,142,143,144,121,122,147,146,170,169,168,145,167,190,166,165,164,163,140,162,185,186,209,208,231,232,233,210,211,187,188,189,212,213,236,235,237,214,215,238,239,240,241,218,217,216,191,192,193,195,194,171,172,173,174,175,196,197,219,220,221,198,199,200,222,224,223,246,247,248,272,271,270,292,269,268,267,245,244,243,242,265,266,290,289,288,264,263,262,286,287,309,310,311,312,334,335,358,357,356,333,355,354,353,352,329,331,332,308,330,307,305,328,351,350,326,327,303,304,281,283,306,284,285,261,260,282,259,258,234,256,254,255,277,257,280,279,278,302,301,300,325,324,323,346,347,348,349,371,370,372,395,394,393,369,392,416,417,415,438,439,440,442,441,420,421,419,418,396,397,375,373,374,376,377,400,399,398,422,423,424,425,401,378,379,380,381,382,405,404,403,402,426,449,450,472,471,448,447,446,470,469,491,468,445,444,443,467,466,490,489,512,511,488,465,464,486,463,462,461,484,485,487,510,509,508,507,530,553,554,555,531,532,556,533,534,535,557,558,559,560,536,513,537,561,562,539,538,515,514,492,516,493,494,517,540,541,518,495,496,519,520,544,543,542,565,564,563,566,567,545,568,546,569,571,573,572,570,547,548,524,525,526,527,549,550,551,574,0,552,528,529,506,483,482,460,459,458,435,436,434,433,432,456,457,479,455,454,453,476,477,478,480,481,505,504,503,502,501,500,523,522,521,499,498,497,475,474,473,452,451,427,428,429,406,407,430,431,408,409,387,410,388,411,412,389,413,414,437,391,390,367,368,366,342,365,341,364,386,363,361,385,384,383,359,360,337,336,313,314,291,293,315,316,339,338,362,340,317,318,294,295,296,297,320,319,343,344,345,322,321,298,299,276,275,274,273,250,251,252,253,230,229,228,227,249,225,226,202,203,179,201,177,176,178,154,155,132,133,156,157,180,182,181,204,205,206,207,184,183,160,161,137,159,158,136,135,134,111,112,113,114,138,115,91,92,90,89,88,87,65,66,67,68,69,45,46,23]
                    cost = 7542.52
                elif algos[k] == "farthest":
                    tour, cost = farthestInsertion(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2", False)
                elif algos[k] == "nearest":
                    tour, cost = nearestNeighbor(sv.rawCoords, sv.guiCoords, sv.cityNames, sv.height, sv.width, "2", False)
                else:
                    tour, cost = randomTour(sv.rawCoords, sv.cityNames, False)

                #print tour info
                end = time.time()
                runtime = end - start

                #run lin-kernighan
                lin(tour, cost, solmax, runtime, "test")
            print("\n")