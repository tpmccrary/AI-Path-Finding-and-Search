# Super class to hold the stats of the algorithms.
class AlgorithmStats:

    def __init__(self):
        self.pathCost = -1
        self.numExpanded = 0
        self.maxNodeInMem = 0
        self.runtime = 0
        self.pathSeq = []

    # Prints the stats.
    def printStats(self):
        print("Cost of the path found: " + str(self.pathCost))
        print("Number of nodes expands: " + str(self.numExpanded))
        print("Max number of nodes in memory: " + str(self.maxNodeInMem))
        print("Runtime: " + str(self.runtime) + "ms")
        if (self.pathSeq == []):
            print("Path to goal: NULL")
        else:
            print("Path to goal: " + str(self.pathSeq))

    # Returns the best path found by BFS.
    def tracePath(self, mapGrid, prevNodes):
        path = []

        node = mapGrid.goalLoc
        while (node != mapGrid.startLoc):
            path.append(node)
            node = prevNodes[str(node)]
            if (node == mapGrid.startLoc):
                path.append(node)
        path.reverse()

        if (path[0] == mapGrid.startLoc):
            return path
        return []



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