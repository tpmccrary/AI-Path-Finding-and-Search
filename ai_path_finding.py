from AI_Path_Finding.map_grid import MapGrid
import AI_Path_Finding
import fileinput

def main():
    # Create new map grid object.
    mapGrid = MapGrid()
    # Get the file from the user input.
    mapFile = fileinput.input()
    # Read the file to grab the details.
    mapGrid.readMapFile(mapFile)



if __name__ == '__main__':
    main()