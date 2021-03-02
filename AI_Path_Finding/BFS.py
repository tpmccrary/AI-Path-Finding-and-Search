from timeit import default_timer as timer
from AI_Path_Finding.algorithm_stats import AlgorithmStats
import queue

# Class for the Breadth first Search algorithm
class BFS(AlgorithmStats):
    
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

    
    # IMPORTANT: The Breadth First Search Algorithm.
    def bfsAlg(self, mapGrid):

        # Timer.
        timeStart = timer()

        # Start and goal locations.
        startLocation = mapGrid.startLoc
        goalLocation = mapGrid.goalLoc

        # Queue, critical for BFS.
        q = queue.Queue()
        q.put(startLocation)

        # Hashtable that holds the path given a node.
        prevNodes = {}

        # Hashtable that holds the cost of a path given a node.
        cost = {}
        cost[str(startLocation)] = 0

        # What nodes we have visited.
        discovered = []
        discovered.append(startLocation)

        # Counter for holding the max number of nodes in the queue.
        maxInMem = 0

        while not q.empty():
            # Logic for determining whats the max number of nodes that was held in the queue.
            if (q.qsize() > maxInMem):
                maxInMem = q.qsize() 
            
            currentNode = q.get()
            
            if (currentNode == goalLocation):
                timeEnd = timer()
                self.pathCost = cost[str(goalLocation)]
                self.numExpanded = len(discovered)
                self.maxNodeInMem = maxInMem
                self.pathSeq = self.tracePath(mapGrid, prevNodes)
                self.runtime = (timeEnd - timeStart) * 1000
                return True

            # Goes thorugh the current nodes neighbors.
            for neighbor in self.getNeighbors(mapGrid, currentNode):
                if (neighbor not in discovered):
                    discovered.append(neighbor)
                    q.put(neighbor)
                    prevNodes[str(neighbor)] = currentNode
                    newCost = cost[str(currentNode)] + mapGrid.grid[neighbor[0]][neighbor[1]]
                
                    if (str(neighbor) not in cost or cost[str(neighbor)] > newCost):
                        cost[str(neighbor)] = cost[str(currentNode)] + mapGrid.grid[neighbor[0]][neighbor[1]]

        # If we reach here, that means the goal was not found.
        timeEnd = timer()
        self.runtime = (timeEnd - timeStart) * 1000
        self.numExpanded = len(discovered)
        self.maxNodeInMem = maxInMem
        return False


    