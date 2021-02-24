from AI_Path_Finding.algorithm_stats import AlgorithmStats
import queue

class BFS(AlgorithmStats):
    
    def __init__(self):
        super().__init__()

    # TODO: 
    # Repeat state checking. Check if the state has been generated before. Keep only the best path.
    # 3 min cut off.
    # For each algorithm print this out:
    #   1. The cost of the path found.
    #   2. The number of nodes expanded.
    #   3. The max num of nodes held in memory.
    #   4. The runntime of the algorithm in milliseconds.
    #   5. The path to goal as a sequence of cordinates.

    # Example of grid:
    # [['2', '4', '2', '1', '4', '5', '2'], 
    #  ['0', '1', '2', '3', '5', '3', '1'], 
    #  ['2', '0', '4', '4', '1', '2', '4'], 
    #  ['2', '5', '5', '3', '2', '0', '1'], 
    #  ['4', '3', '3', '2', '1', '0', '1']]
    # Start: row: 1 col: 2
    # Gaol:  row: 4 col: 3
    
    def bfsAlg(self, mapGrid):
        startLocation = mapGrid.startLoc
        goalLocation = mapGrid.goalLoc

        q = queue.Queue()
        q.put(startLocation)
        prevNodes = {}

        cost = {}
        cost[str(startLocation)] = 0

        discovered = []
        discovered.append(startLocation)

        maxInMem = 0

        while not q.empty():

            if (q.qsize() > maxInMem):
                maxInMem = q.qsize() 
            
            currentNode = q.get()
            
            if (currentNode == goalLocation):
                # BFS.tracePath(mapGrid, prevNodes)
                # print(BFS.tracePath(mapGrid, prevNodes))
                self.pathCost = cost[str(goalLocation)]
                self.numExpanded = len(discovered)
                self.maxNodeInMem = maxInMem
                self.pathSeq = self.tracePath(mapGrid, prevNodes)
                return True

            for neighbor in BFS.getNeighbors(mapGrid, currentNode):
                if (neighbor not in discovered):
                    discovered.append(neighbor)
                    q.put(neighbor)
                    prevNodes[str(neighbor)] = currentNode
                    newCost =cost[str(currentNode)] + mapGrid.grid[neighbor[0]][neighbor[1]]
                
                    if (str(neighbor) not in cost or cost[str(neighbor)] > newCost):
                        cost[str(neighbor)] = cost[str(currentNode)] + mapGrid.grid[neighbor[0]][neighbor[1]]

        return False


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
        


    def getNeighbors(mapGrid, currentNode):
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
    