from AI_Path_Finding.map_grid import MapGrid
import AI_Path_Finding
import fileinput
from AI_Path_Finding.BFS import BFS
import sys

def main():
    if (len(sys.argv) != 3):
        print("Incorrect commands.\nPlease enter: <filepath>.txt <searching_algorithm>\nExiting...")
        sys.exit(1)

    fileName = sys.argv[1]
    algorithm = sys.argv[2]
    
    
    
    # TODO: Get input for algorithm type (i.e. BFS, IDS)
    # Get the file from the user input.
    mapFile = fileinput.input(fileName)
    # Create new map grid object.
    mapGrid = MapGrid(mapFile)

    if (algorithm == "BFS"):
        print("Using BFS.")
        BFS.bfs(mapGrid)
    else:
        print("Please enter: BFS")
        sys.exit(1)

    

    



if __name__ == '__main__':
    main()