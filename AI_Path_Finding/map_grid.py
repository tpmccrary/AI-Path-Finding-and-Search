class MapGrid:
    height = 0
    width = 0
    startLoc = []
    goalLoc = []
    grid = []

    def __init__(self) -> None:
        pass

    @staticmethod
    def readMapFile(mapFile):
        if (mapFile == None or mapFile == ""):
            print("No file given. Exiting...")
            exit(1)
        print("Reading map file...")

        for line in mapFile:
            print(line)
            

        return