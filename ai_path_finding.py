from AI_Path_Finding.map_grid import MapGrid
import fileinput
from AI_Path_Finding.BFS import BFS
from AI_Path_Finding.ids import IDS
from AI_Path_Finding.a_star import AStar
import sys
import signal

def main():
    # Checks the user inputed the right command.
    if (len(sys.argv) != 3):
        print("Incorrect commands.\nPlease enter: <filepath>.txt <searching_algorithm>\nExiting...")
        sys.exit(1)
    
    # Get the arguments from user.
    fileName = sys.argv[1]
    algorithm = sys.argv[2]
        
    # Get the file from the user input.
    mapFile = fileinput.input(fileName)
    # Create new map grid object.
    mapGrid = MapGrid(mapFile)

    # Breadth First Search
    if (algorithm == "BFS"):
        useBFS(mapGrid)
    # Iterative Deepening Search
    elif (algorithm == "IDS"):
        useIDS(mapGrid)
    # A Star Search
    elif (algorithm == "AS"):
        useAStar(mapGrid)
    else:
        print("Please enter: BFS, IDS, or AS for algorihtm command.")
        sys.exit(1)

# Where AStar is called.
def useAStar(mapGrid):
    print("Using A*.")
    aStar = AStar()
    # Flag if the algorithm found the goal.
    foundGoal = False
    # Sets timout for 3min
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(180)
    # IMPORTANT: This is where the actaul AS algorithm is called.
    try:
        foundGoal = aStar.aStar(mapGrid)
    except Exception:
        print("FAILURE: Program Timed Out: 3min")
    signal.alarm(0)
    if (foundGoal):
        print("SUCCESS.")
    else:
        print("FAILURE: Could not find path.")
    aStar.printStats()

# Where IDS is called.
def useIDS(mapGrid):
    print("Using IDS.")
    # The ids object.
    ids = IDS()

    # Flag if the algorithm found the goal.
    foundGoal = False

    # Sets timout for 3min
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(180)
    try:
        # IMPORTANT: This is where the actual IDS algorithm is called.
        foundGoal = ids.depthLimitedSearch(mapGrid, 0)
    except Exception:
        print("FAILURE: Program Timed Out: 3min")
    # Set the timout to 0.
    signal.alarm(0)

    if (foundGoal):
        print("SUCCESS.")
    else:
        print("FAILURE: Could not find path.")

    # This prints the stats of the algorithm.
    ids.printStats()

# Where BFS is called.
def useBFS(mapGrid):
    print("Using BFS.")
    # Create BFS object.
    bfs = BFS()

    # Flag to determine if algorithm found the goal.
    foundGoal = False

    # Sets timout for 3min
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(180)
    try:
        # IMPORTANT: This is where the actual BFS algorithm is called.
        foundGoal = bfs.bfsAlg(mapGrid)
    except Exception:
        print("FAILURE: Program Timed Out: 3min")
    # Set the timout to 0.
    signal.alarm(0)

    if (foundGoal):
        print("SUCCESS.")
    else:
        print("FAILURE: Could not find path.")
    # Prints the stats from the algorithm.
    bfs.printStats()

# Not sure what this does, but it handles the timeout (alarm).   
def handler(signum, frame):
    print("Forever is over!")
    raise Exception("end of time")
    



if __name__ == '__main__':
    main()