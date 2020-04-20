from solve import *
from randTest import *
from genTest import *          

if __name__ == "__main__":
    #clear the console
    clear = lambda: os.system('cls')
    clear()

    #accept input
    print("""Enter a method by its number (default method 1):
    1: Solve single problem with GUI
    2: Benchmarking. Solve every problem with every generation algorithm and SOLMAX
    3: Benchmarking. Solve single problem with sets of randomly generated tours\n""")
    method = input()
    clear()

    #run either the tests or problem solver
    if method == "2":
        genTest()
    elif method == "3":
        randTest()
    else:
        solve()