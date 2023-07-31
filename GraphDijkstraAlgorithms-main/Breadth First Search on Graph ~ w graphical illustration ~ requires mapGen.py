import turtle
import time
from mapGen import *

class Queue(object):
    
    def __init__(self):
        self._queue = []
        
    def enQueue(self, item):
        self._queue.append(item)
        
    def deQueue(self):
        try:
            return self._queue.pop(0)
        except IndexError as e:
            raise IndexError('Empty Queue')
            
    def __len__(self):
        return len(self._queue)
    
    def __str__(self):
        return str(self._queue)
            
class BFS(object):
    
    def __init__(self, mapOfGraph, size):
        self._map = mapOfGraph
        self._size = size
        
    def __drawNode(self, i, colour = 'white'):
        if isinstance(i, tuple):
            self._pen.setpos((i[0]-self._size/2)*300/self._size,(i[1]-self._size/2)*300/self._size)
            self._pen.fillcolor(colour)
            self._pen.pencolor(colour)
            self.__drawSquare()
        
    def __drawSquare(self):
        self._pen.down()
        self._pen.begin_fill()
        for i in range(4):
            self._pen.forward(300/self._size)
            self._pen.right(90)
        self._pen.end_fill()
        self._pen.up()
        
    def drawMap(self):
        self._window = turtle.Screen()
        self._window.clear()
        self._window.bgcolor('black')
        self._pen = turtle.Turtle()
        self._pen.up()
        self._pen.speed(0)
        self._pen.pencolor('white')
        for i in range(self._size):
            self._pen.setpos((i-self._size/2)*300/self._size, (-2-self._size/2)*300/self._size)
            self._pen.write(i)
        for i in range(self._size+1):
            self._pen.setpos((-1-self._size/2)*300/self._size, (i-1-self._size/2)*300/self._size)
            self._pen.write(i)
        for i in self._map:
            self.__drawNode(i)
        
    def fastestRoute(self, startNode, endNode):
        
        self._visited = {}
        for i in self._map.keys():
            self._visited[i] = 'WHYDOES0BECOMEFALSE'
        self._queue = Queue()
        self._queue.enQueue(startNode)
        self._visited[startNode]='Start'
        self.__drawNode(startNode, 'blue')
        self.__drawNode(endNode, 'blue')
        foundEnd=False
        while len(self._queue)>0 and not(foundEnd):
            currentNode= self._queue.deQueue()
            if currentNode!=startNode:
                self.__drawNode(currentNode,'green')
            for i in self._map[currentNode]:
                if self._visited[i]=='WHYDOES0BECOMEFALSE':
                    self._visited[i]=currentNode
                    self._queue.enQueue(i)
                    if i ==endNode:
                        foundEnd=True
        self.__drawNode(endNode, 'green')
                    
        path = [self._visited[endNode],endNode]
        end=False
        while not(end):
            if path[0]=='Start':
                end=True
            else:
                path.insert(0,self._visited[path[0]])
                
        for i in path:
            self.__drawNode(i, 'red')
            
        return path
        
def validateInput(text, l):
    print(text)
    valid = False
    while not(valid):
        userInput = input('--> ')
        if userInput in l:
            valid = True
    return userInput

while True:
    a = generateDungeon(input('Seed --> '),int(input('Map Size --> '))+1)
    b = BFS(a.getMap(), a.getSize())
    b.drawMap()
    option = validateInput('What option? (\'random\', \'default\', or \'choose\')',['random','default','choose'])
    if option == 'choose':
        start = (int(input('X coord of start --> ')),int(input('y coord of start --> ')))
        end = (int(input('X coord of end --> ')),int(input('y coord of end --> ')))
    elif option == 'random':
        aMap = list(a.getMap().keys())
        random.seed(time.clock())
        start = aMap.pop(random.randint(0, len(aMap)-1))
        end = aMap.pop(random.randint(0, len(aMap)-1))
    elif option == 'default':
        start = a.getStart()
        end = a.getEnd()
    
    try:
        b.fastestRoute(start, end)
    except IndexError:
        print('Something went wrong!')
