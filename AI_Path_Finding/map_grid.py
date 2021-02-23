class MapGrid:
    def __init__(self, mapFile):
        self.height = 0
        self.width = 0
        self.startLoc = []
        self.goalLoc = []
        self.grid = []
        self.readMapFile(mapFile)

    # Given a map file, record its data.
    def readMapFile(self, mapFile):
        if (mapFile == None or mapFile == ""):
            print("No file given. Exiting...")
            exit(1)
        print("Reading map file...")

        lineNum = 0
        # We go through every line in the data.
        for line in mapFile:
            # If it is the first line, get the heigh and width.
            if (lineNum == 0):
                splitLine = line.split()
                self.height = splitLine[0]
                self.width = splitLine[1]
            # If it is the seconds line, get the starting location.
            elif (lineNum == 1):
                splitLine = line.split()
                self.startLoc.append(splitLine[0])
                self.startLoc.append(splitLine[1])
            # If it is the third line, get the goal location.
            elif (lineNum == 2):
                splitLine = line.split()
                self.goalLoc.append(splitLine[0])
                self.goalLoc.append(splitLine[1])
            elif (lineNum >= 3):
                splitLine = line.split()
                self.grid.append(splitLine)

            lineNum += 1
        
        return