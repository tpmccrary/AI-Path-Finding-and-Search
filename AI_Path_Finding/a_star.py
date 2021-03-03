from AI_Path_Finding.algorithm_stats import AlgorithmStats
from timeit import default_timer as timer


# This class holds the logic for A* Algorithm.
class AStar(AlgorithmStats):

    def __init__(self):
        super().__init__()

    # Example of grid:
    # [['2', '4', '2', '1', '4', '5', '2'], 
    #  ['0', '1', '2', '3', '5', '3', '1'], 
    #  ['2', '0', '4', '4', '1', '2', '4'], 
    #  ['2', '5', '5', '3', '2', '0', '1'], 
    #  ['4', '3', '3', '2', '1', '0', '1']]
    # Start: row: 1 col: 2
    # Gaol:  row: 4 col: 3
    
    # Actual A* algorithm.
    def aStar(self, mapGrid):

        timeStart = timer()

        # Nodes that have been discovered and we might have to look through them.
        discovered = []
        discovered.append(mapGrid.startLoc)

        # Hashtable that given a key, it points to the node it came from.
        prevNodes = {}

        # The gScore[n] (i.e. gScore[[1, 2]]) is the cost of the cheapest path from start to n.
        gScore = {}
        gScore[str(mapGrid.startLoc)] = 0

        # The fScore[n] best guess cost from start to goal including n.
        fScore = {}
        fScore[str(mapGrid.startLoc)] = self.heuristic(mapGrid.startLoc, mapGrid)


        while len(discovered) > 0:
            
            # Records max number of nodes held in memory.
            if (len(discovered) > self.maxNodeInMem):
                self.maxNodeInMem = len(discovered)

            currentNode = []
            # Gets the best node (best fScore) in the discovered list.
            for node in discovered:
                if (currentNode == [] or fScore[str(node)] < mapGrid.grid[currentNode[0]][currentNode[1]]):
                    currentNode = node
            
            # Check for goal.
            if currentNode == mapGrid.goalLoc:
                timeEnd = timer()
                self.pathCost = gScore[str(currentNode)]
                self.numExpanded = len(prevNodes)
                self.pathSeq = self.tracePath(mapGrid, prevNodes)
                self.runtime = (timeEnd - timeStart) * 1000
                return True

            discovered.remove(currentNode)
            for neighbor in self.getNeighbors(mapGrid, currentNode):
                # Tentative goal, the cost from current node to the neighbor.
                tent_gScore = gScore[str(currentNode)] + mapGrid.grid[neighbor[0]][neighbor[1]]

                # If the path to the neighbor is better thant the previous, rememeber it.
                if str(neighbor) not in gScore or tent_gScore < gScore[str(neighbor)]:
                    prevNodes[str(neighbor)] = currentNode
                    gScore[str(neighbor)] = tent_gScore
                    fScore[str(neighbor)] = gScore[str(neighbor)] + self.heuristic(neighbor, mapGrid)

                    if neighbor not in discovered:
                        discovered.append(neighbor)

        timeEnd = timer()
        self.numExpanded = len(prevNodes)
        self.runtime = (timeEnd - timeStart) * 1000
        return False

    # Manhattan Distance heuristic. abs(x1 - x2) + abs(y1 - y2)
    def heuristic(self, node, mapGrid):
        return abs(node[0] - mapGrid.goalLoc[0]) + abs(node[1] - mapGrid.goalLoc[1])
