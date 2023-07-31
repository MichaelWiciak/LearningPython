import turtle
import time
turtle.ht()
turtle.pu()
turtle.speed(0)

class Conway(object):
    def rules(self, grid):
        coords = grid.getCoords()
        for x in coords.keys():
            for y in coords[x]:
                cellCount = self.__checkCells(x, y, coords, "count")
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        cellExists = self.__checkCells(x+i, y+j, coords, "exists")
                        if not(cellExists):
                            newCellCount = self.__checkCells(x+i, y+j, coords, "count")
                            if newCellCount == 3:
                                grid.addCoords(x+i, y+j)
                if cellCount < 2 or cellCount > 3:
                    grid.removeCoords(x, y)

    def __checkCells(self, x, y, coords, control):
        if control == "count":
            cellCount = 0
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                        if x+i in coords.keys() and y+j in coords[x+i] and not(i == 0 and j == 0):
                            cellCount += 1
            return cellCount
        if control == "exists":
            if x in coords.keys() and y in coords[x]:
                return True
            return False

class Grid(object):
    def __init__(self):
        self.__coords = {}
        self.__updateCoords = {}

    def addCoords(self, x, y):
        if x not in self.__updateCoords.keys():
            self.__updateCoords[x] = []
        if y not in self.__updateCoords[x]:
            self.__updateCoords[x].append(y)

    def removeCoords(self, x, y):
        self.__updateCoords[x].remove(y)
        if self.__updateCoords[x] == []:
            del(self.__updateCoords[x])

    def getCoords(self):
        return self.__coords

    def updateCoords(self):
        self.__coords = {}
        for x in self.__updateCoords.keys():
            for y in self.__updateCoords[x]:
                if x not in self.__coords.keys():
                    self.__coords[x] = []
                self.__coords[x].append(y)

class Visual(object):
    def __init__(self, grid, scale):
        coords = grid.getCoords()
        turtle.tracer(0,0)
        turtle.clear()
        for x in coords.keys():
            for y in coords[x]:
                turtle.setx(x*scale)
                turtle.sety(y*scale)
                turtle.begin_fill()
                for i in range(4):
                    turtle.fd(scale)
                    turtle.bk(1)
                    turtle.right(90)
                turtle.end_fill()

class App(object):
    def __init__(self):
        self.__grid = Grid()
        openFile = input("Type 'OPEN' to open a .cgl file (or press ENTER to continue)\n>>> ").upper()
        if openFile == "OPEN":
            fileName = input("\nEnter the name of your file\n>>> ")
            file = open(fileName, "r")
            coordList = file.read()
            coordList = coordList.split("\n")
            for coords in coordList:
                coord = coords.split(",")
                self.__grid.addCoords(int(coord[0]), int(coord[1]))
            self.__grid.updateCoords()
            file.close()
        done = False
        while not(done):
            self.__scaleFactor = input("\nWhat scale factor would you like to use? (Min. of 1) (Max. of 10)\n>>> ")
            if not(self.__scaleFactor.isdigit()) or int(self.__scaleFactor) < 1 or int(self.__scaleFactor) > 10:
                print("\nError")
            else:
                self.__scaleFactor = int(self.__scaleFactor)
                done = True
        Visual(self.__grid, self.__scaleFactor)
        turtle.update()
        complete = False
        while not(complete):
            newCoord = input("\nInput a new coordinate in the format x,y (e.g. 5,6) or type 'RUN' to continue\n>>> ").upper()
            if newCoord == "RUN":
                complete = True
            else:
                newCoord = newCoord.split(",")
                self.__grid.addCoords(int(newCoord[0]), int(newCoord[1]))
                self.__grid.updateCoords()
                Visual(self.__grid, self.__scaleFactor)
                turtle.update()
        saveFile = input("\nType 'SAVE' to save your coordinates in a file (or press ENTER to continue)\n>>> ").upper()
        if saveFile == "SAVE":
            coords = self.__grid.getCoords()
            coordList = []
            for x in coords.keys():
                for y in coords[x]:
                    coordList.append(str(x)+","+str(y))
            coordList = "\n".join(coordList)
            fileName = input("\nWhat would you like to name your file?\n>>> ")
            file = open(fileName+".cgl", "w")
            file.write(coordList)
            file.close()

    def update(self):
        updateCells = Conway()
        while True:
            Visual(self.__grid, self.__scaleFactor)
            turtle.update()
            updateCells.rules(self.__grid)
            self.__grid.updateCoords()
            time.sleep(0.1)

app = App()
app.update()
