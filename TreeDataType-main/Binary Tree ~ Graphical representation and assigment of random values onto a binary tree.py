from binaryTree import *
import turtle
import random

def balanced():
    tree = BinaryTree(0)
    priorNodes = [0]
    for i in range(5):
        newNodes = []
        for j in priorNodes:
            newNodes.append(j+128*2**(-i))
            newNodes.append(j-128*2**(-i))
        priorNodes = newNodes
        for j in priorNodes:
            tree.insert(j)
        
    return tree

def unbalanced():
    listOfStuff = None
    for i in range(0,10):
        listOfStuff=[i,listOfStuff,None]
    return BinaryTree(listOfStuff, True)

class MainApp(object):
    
    binaryTreeMap = {'Equation':BinaryTree(['*',['+',5,2],['-',['^',2,-2],4]], True),'Unbalanced':unbalanced(),'Balanced':balanced()}
    
    def __init__(self):
        self._window = turtle.Screen()
        self._pen = turtle.Turtle()
        
        while True:
            dataForTree, speed = self.__takeInput()
                
            self._pen.clear()
            self._pen.speed(speed)
            if isinstance(dataForTree, int):
                tree = BinaryTree(random.randint(-1000,1000))
                listOfStuffForTree = []
                for i in range(dataForTree-1):
                    listOfStuffForTree.append(random.randint(-1000,1000))
                for i in listOfStuffForTree:
                    tree.insert(i)
            else:
                tree = dataForTree
            t = Traverser(tree, self._pen)
            
    def __takeInput(self):
        
        userInput = input('Do you want to use a pre-made tree (y/anything else) --> ')
        if userInput == 'y':
            validInput = False
            while not(validInput):
                print(list(MainApp.binaryTreeMap.keys()))
                userInput = input('Which tree --> ')
                if userInput in MainApp.binaryTreeMap.keys():
                    validInput = True
                    tree = MainApp.binaryTreeMap[userInput]
        else:
            validInput = False
            while not(validInput):
                userInput = input('Enter an integer between 1 and 100 (number of items)--> ')
                try:
                    tree = int(userInput)
                    if tree>=1 and tree<=1000:
                        validInput = True
                except TypeError:
                    pass
        validInput = False
        while not(validInput):
            userInput = input('Choose a speed between 1 and 10 --> ')
            try:
                speed = int(userInput)
                if speed>=1 and speed<=10:
                    validInput = True
            except TypeError:
                pass
        
        return tree, speed
        
class Traverser(object):
    
    def __init__(self, tree, turt):
        '''Traverses the tree and displays using turtle'''
        self._pen = turt
        self._pen.penup()
        self._pen.setx(0)
        self._pen.sety(250)
        
        self._stackOfCoords = [(0,250)]
        self.__search(tree)
        
    def __search(self, tree):
        item = tree.getRoot()
        self._pen.write(item)
        if tree.getLeftChild() != None:
            self._pen.pencolor('red')
            self._pen.pendown()
            coords = (self._pen.xcor()-(600/(2**len(self._stackOfCoords))), self._pen.ycor()-40)
            self._stackOfCoords.append(coords)
            self._pen.setpos(coords)
            self._pen.penup()
            self._pen.color('black')
            self.__search(tree.getLeftChild())
            self._pen.setpos(self._stackOfCoords[-1])
        if tree.getRightChild() != None:
            self._pen.pencolor('red')
            self._pen.pendown()
            coords = (self._pen.xcor()+(600/(2**len(self._stackOfCoords))), self._pen.ycor()-40)
            self._stackOfCoords.append(coords)
            self._pen.setpos(coords)
            self._pen.penup()
            self._pen.color('black')
            self.__search(tree.getRightChild())
            self._pen.setpos(self._stackOfCoords[-1])
        self._stackOfCoords.pop()
            
            
        
a = MainApp()