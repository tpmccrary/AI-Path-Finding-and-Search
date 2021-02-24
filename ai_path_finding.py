from AI_Path_Finding.map_grid import MapGrid
import AI_Path_Finding
import fileinput
from AI_Path_Finding.BFS import BFS

def main():
    # TODO: Get input for algorithm type (i.e. BFS, IDS)
    # Get the file from the user input.
    mapFile = fileinput.input()
    # Create new map grid object.
    mapGrid = MapGrid(mapFile)

    # Example:
    print("The starting point: " + str(mapGrid.startLoc))
    print("The goal: " + str(mapGrid.goalLoc))

    BFS.bfs(mapGrid)

    



if __name__ == '__main__':
    main()