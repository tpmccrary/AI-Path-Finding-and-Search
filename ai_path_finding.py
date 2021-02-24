from AI_Path_Finding.map_grid import MapGrid
import AI_Path_Finding
import fileinput
from AI_Path_Finding.BFS import BFS
import sys
import subprocess

def main():
    if (len(sys.argv) != 3):
        print("Incorrect commands.\nPlease enter: <filepath>.txt <searching_algorithm>\nExiting...")
        sys.exit(1)

    fileName = sys.argv[1]
    algorithm = sys.argv[2]
        
    # Get the file from the user input.
    mapFile = fileinput.input(fileName)
    # Create new map grid object.
    mapGrid = MapGrid(mapFile)

    if (algorithm == "BFS"):
        print("Using BFS.")
        bfs = BFS()
        foundGoal = False
        try:
            r = subprocess.run(['echo'], timeout=3)
            foundGoal = bfs.bfsAlg(mapGrid)
        except subprocess.TimeoutExpired:
            print("Program Timed Out: 3min")
        
        if (foundGoal):
            print("SUCCESS.")
        else:
            print("FAILURE: Could not find path.")

        bfs.printStats()
    if (algorithm == "IDS"):
        print("IDS under development.\nExiting...")
    else:
        print("Please enter: BFS")
        sys.exit(1)

    

    



if __name__ == '__main__':
    main()