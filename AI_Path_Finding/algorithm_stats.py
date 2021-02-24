class AlgorithmStats:

    def __init__(self):
        self.pathCost = -1
        self.numExpanded = 0
        self.maxNodeInMem = 0
        self.runtime = 0
        self.pathSeq = []

    def printStats(self):
        print("Cost of the path found: " + str(self.pathCost))
        print("Number of nodes expands: " + str(self.numExpanded))
        print("Max number of nodes in memory: " + str(self.maxNodeInMem))
        print("Runtime: " + str(self.runtime) + "ms")
        if (self.pathSeq == []):
            print("Path to goal: NULL")
        else:
            print("Path to goal: " + str(self.pathSeq))