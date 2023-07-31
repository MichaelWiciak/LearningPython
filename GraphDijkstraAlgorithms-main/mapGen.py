import random

class MapGenerator(object):
    
    def __init__(self, seed, lengthOfMap):
        random.seed(seed)
        self._length = lengthOfMap
        
    def generateMap(self):
        aMap = {}
        for i in range(self._length):
            aMap[i]=[]
        for i in range(self._length):
            connections = aMap[i]
            try:
                numberOfNodes = random.randint(1,3-len(connections))
            except:
                numberOfNodes = 0
            nodesToChoose = list(range(0,self._length))
            nodesToChoose.remove(i)
            for j in connections:
                nodesToChoose.remove(j[0])
            for j in range(numberOfNodes):
                newNode = nodesToChoose.pop(random.randint(0,len(nodesToChoose)-1))
                distance = random.randint(1,30)
                connections.append([newNode, distance])
                aMap[newNode].append([i, distance])
            aMap[i]=connections
        return aMap
    
class generateDungeon(object):
    
    def __init__(self, seed, gridSize):
        self._size = gridSize
        random.seed(seed)
        self._grid = {}
        self._start = (random.randint(0,gridSize-1),0)
        self._grid[self._start]=[]
        self._blacklist = [self._start]
        self._whitelist = [[(self._start[0],self._start[1]+1),self._start]]
        
        self._topList = []
        
        while len(self._whitelist)>0:
            self.__createNewNode()
            
        exitCoords = random.choice(self._topList)
        coords = (exitCoords[0], exitCoords[1]+1)
        self._grid[exitCoords].append(coords)
        self._grid[coords]=[exitCoords]
        self._end = coords

        self.__createCycles()
        
    def __createCycles(self):
        possibleNodes = []
        for i in self._blacklist:
            if not(i in self._grid.keys()):
                possibleNodes.append(i)
                
        numberToChoose = random.randint(1,len(possibleNodes)//5)
        for i in range(numberToChoose):
            self.__createNode(possibleNodes.pop(random.randint(0, len(possibleNodes)-1)))
            
    def __createNode(self, coords):
        nodesToConnectTo = [(coords[0],coords[1]+1),(coords[0],coords[1]-1),(coords[0]+1,coords[1]),(coords[0]-1,coords[1])]
        edges = []
        for i in nodesToConnectTo:
            if i in self._grid.keys():
                self._grid[i].append(coords)
                edges.append(i)
        self._grid[coords]=edges
        
    def __createNewNode(self):
        coordsAndSource = self._whitelist.pop(random.randint(0,len(self._whitelist)-1))
        self._grid[coordsAndSource[1]].append(coordsAndSource[0])
        self._blacklist.append(coordsAndSource[0])
        self._grid[coordsAndSource[0]]=[coordsAndSource[1]]
        connections = [(coordsAndSource[0][0],coordsAndSource[0][1]+1),(coordsAndSource[0][0],coordsAndSource[0][1]-1),(coordsAndSource[0][0]+1,coordsAndSource[0][1]),(coordsAndSource[0][0]-1,coordsAndSource[0][1])]
        edges = []
        for i in connections:
            if self.__checkFor(i):
                self._whitelist.pop(self._destroyNodeLocation)
            elif not(i in self._blacklist) and i[0]<self._size and i[0]>=0 and i[1]<self._size and i[1]>0:
                edges.append(i)
                self._blacklist.append(i)
                self._whitelist.append([i,coordsAndSource[0]])
        
        if coordsAndSource[0][1]==self._size-1:
            self._topList.append(coordsAndSource[0])
    
    def __checkFor(self, coords):
        there = False
        count = 0
        while not(there) and count<len(self._whitelist):
            if coords == self._whitelist[count][0]:
                there = True
            else:
                count+=1
                
        self._destroyNodeLocation = count
        return there
                    
    def getMap(self):
        return self._grid
    
    def getStart(self):
        return self._start
    
    def getEnd(self):
        return self._end
    
    def getSize(self):
        return self._size