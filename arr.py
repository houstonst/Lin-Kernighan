from lkUtils import *

class Vert:
    def __init__(self, array, added, removed, gainSum):
        self.array = array
        self.added = added
        self.removed = removed
        self.gainSum = gainSum
    def info(self):
        print("""Path: {}
added: {}
removed: {}
gainSum: {}\n""".format(stringify(self.array), self.added, self.removed, self.gainSum))

class Tour:
    def __init__(self, array, cost):
        self.array = array
        self.cost = cost
    def info(self):
        print("Tour: {}, Cost: {}\n".format(stringify(self.array), self.cost))