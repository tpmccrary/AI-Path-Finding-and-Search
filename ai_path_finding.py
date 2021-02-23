from AI_Path_Finding.map_grid import MapGrid
import AI_Path_Finding
import fileinput

def main():
    # Get the file from the user input.
    mapFile = fileinput.input()
    # Create new map grid object.
    mapGrid = MapGrid(mapFile)
    



if __name__ == '__main__':
    main()