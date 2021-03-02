from AI_Path_Finding.algorithm_stats import AlgorithmStats
from timeit import default_timer as timer


# This class holds the logic for Iterative Deepening Search.
class IDS(AlgorithmStats):
    
    def __init__(self):
        # We initialize these two variables to remeber if we have been to a node.
        # We have two so we can compare them to eachother and check if we have gone through the entire grid.
        # Other variables are for recording algorithm stats and comparing.
        self.discoverd = []
        self.lastDisc = []
        self.cost = {}
        self.prevNodes = {}
        self.maxNodes = 0
        self.timerStart = 0
        self.timeEnd = 0
        super().__init__()


    # Example of grid:
    # [['2', '4', '2', '1', '4', '5', '2'], 
    #  ['0', '1', '2', '3', '5', '3', '1'], 
    #  ['2', '0', '4', '4', '1', '2', '4'], 
    #  ['2', '5', '5', '3', '2', '0', '1'], 
    #  ['4', '3', '3', '2', '1', '0', '1']]
    # Start: row: 1 col: 2
    # Gaol:  row: 4 col: 3

    # This is the itterative deepening algorithm. We start at a limit, and iteravlity go up.
    def depthLimitedSearch(self, mapGrid, limit):
        # Timer.
        self.timeStart = timer()

        while True:
            # Add starting location to the discovered list.
            self.discoverd.append(mapGrid.startLoc)
            self.cost[str(mapGrid.startLoc)] = 0

            # print("***ITERATION: " + str(limit) + "***")
            # Call the DLS algorithm with given limit.
            # If it returns True, we found the goal, else it returns false.
            if (self.recursiveDLS(mapGrid.startLoc, mapGrid, limit)):
                self.pathCost = self.cost[str(mapGrid.goalLoc)]
                self.pathSeq = self.tracePath(mapGrid, self.prevNodes)
                self.numExpanded = len(self.discoverd)
                self.timeEnd = timer()
                self.runtime = (self.timeEnd - self.timeStart) * 1000
                return True

            # If the discovered list is the same as the discovered list for the previous iteration, that means we have gone through
            # all the nodes and the goal was not found.
            if (self.discoverd == self.lastDisc):
                self.maxNodeInMem = self.maxNodes
                self.timeEnd = timer()
                self.runtime = (self.timeEnd - self.timeStart) * 1000
                return False
            
            # The current discovered list is saved here so we can compare later.
            self.lastDisc = self.discoverd

            # Reset the discovered list for the new iteration.
            self.discoverd = []
            self.cost = {}
            self.prevNodes = {}
            self.maxNodes = 0
            self.maxNodeInMem = 0

            limit += 1

    

    # This is depth limited search done recursively.
    # It is done recursively so we can "remember" the previous limits.
    def recursiveDLS(self, currentNode, mapGrid, limit):

        # print("Current Node: " + str(currentNode) + " at level:  " + str(limit))
        # Check if the current node is our goal.
        if (currentNode == mapGrid.goalLoc):
            return True

        # Check if we have reached the limit (we are counting down).
        if limit <= 0:
            return False
        
        # Go through every neighbor. This list acts like a stack. Thats why it is reversed.
        # We are pretty much building a stack recursively.
        for neighbor in reversed(self.getNeighbors(mapGrid, currentNode)):
            if (neighbor not in self.discoverd):
                # print(str(neighbor) + " at level: " + str(limit))
                self.discoverd.append(neighbor)
                
                # This is the check for the max number of nodes in memeory.
                self.maxNodes += 1
                if (self.maxNodes > self.maxNodeInMem):
                    self.maxNodeInMem = self.maxNodes

                # Hashtable reconstructs the path from node.
                self.prevNodes[str(neighbor)] = currentNode
                
                # Hashtable that stores how much it cost to get to that position.
                newCost = self.cost[str(currentNode)] + mapGrid.grid[neighbor[0]][neighbor[1]]
                
                if (str(neighbor) not in self.cost or self.cost[str(neighbor)] > newCost):
                    self.cost[str(neighbor)] = self.cost[str(currentNode)] + mapGrid.grid[neighbor[0]][neighbor[1]]

                # Call the DLS again but we count down the limit.
                if (self.recursiveDLS(neighbor, mapGrid, limit - 1)):
                    return True
        return False


    

    