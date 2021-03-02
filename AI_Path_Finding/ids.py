from AI_Path_Finding.algorithm_stats import AlgorithmStats

class IDS(AlgorithmStats):
    
    def __init__(self):
        self.discoverd = []
        self.lastDisc = []
        super().__init__()


    # Example of grid:
    # [['2', '4', '2', '1', '4', '5', '2'], 
    #  ['0', '1', '2', '3', '5', '3', '1'], 
    #  ['2', '0', '4', '4', '1', '2', '4'], 
    #  ['2', '5', '5', '3', '2', '0', '1'], 
    #  ['4', '3', '3', '2', '1', '0', '1']]
    # Start: row: 1 col: 2
    # Gaol:  row: 4 col: 3

    # TODO:
    # Cost of path found.
    # Number of nodes expanded. (discovered)
    # Max in memory. (stack)
    # Runtime
    # Path

    # This is the itterative deepening function. We start at a limit, and iteravlity go up.
    def depthLimitedSearch(self, mapGrid, limit):

        while True:
            # Add starting location to the discovered list.
            self.discoverd.append(mapGrid.startLoc)

            # print("***ITERATION: " + str(limit) + "***")
            # Call the DLS algorithm with given limit.
            # If it returns True, we found the goal, else it returns false.
            if (self.recursiveDls(mapGrid.startLoc, mapGrid, limit)):
                return True

            # If the discovered list is the same as the discovered list for the previous iteration, that means we have gone through
            # all the nodes and the goal was not found.
            if (self.discoverd == self.lastDisc):
                return False
            
            # The current discovered list is saved here so we can compare later.
            self.lastDisc = self.discoverd

            # Reset the discovered list for the new iteration.
            self.discoverd = []

            limit += 1


    # This is depth limited search done recursively.
    # It is done recursiley so we can "remember" the previous limits.
    def recursiveDls(self, currentNode, mapGrid, limit):

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
                # Call the DLS again but we count down the limit.
                if (self.recursiveDls(neighbor, mapGrid, limit - 1)):
                    return True
        return False




    # Gets the neighbors given the node and the grid.
    def getNeighbors(self, mapGrid, currentNode):
        neighbors = []
        nodeRow = currentNode[0]
        nodeCol = currentNode[1]

        # top
        if (nodeRow - 1 >= 0 and mapGrid.grid[nodeRow - 1][nodeCol] != 0):
            top = [nodeRow - 1, nodeCol]
            neighbors.append(top)

        # bottom
        if (nodeRow + 1 < mapGrid.height and mapGrid.grid[nodeRow + 1][nodeCol] != 0):
            bottom = [nodeRow + 1, nodeCol]
            neighbors.append(bottom)

        # right
        if(nodeCol + 1 < mapGrid.width and mapGrid.grid[nodeRow][nodeCol + 1] != 0):
            right = [nodeRow, nodeCol + 1]
            neighbors.append(right)

        #left
        if (nodeCol - 1 >= 0 and mapGrid.grid[nodeRow][nodeCol - 1] != 0):
            left = [nodeRow, nodeCol - 1]
            neighbors.append(left)

        return neighbors

    