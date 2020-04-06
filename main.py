from solve import *
from randTest import *
from genTest import *          

if __name__ == "__main__":
    #clear the console
    clear = lambda: os.system('cls')
    clear()

    #accept input
    print("Enter a .csv or .txt file [example.csv or example.txt]. Alternatively, enter 'test1' or 'test2 in order to benchmark:\n")
    inp = input()
    clear()

    #run either the tests or problem solver
    if inp == "test1":
        test1()
    elif inp == "test2":
        test2()
    else:
        filepath = "./tests/" + inp
        solve(filepath)