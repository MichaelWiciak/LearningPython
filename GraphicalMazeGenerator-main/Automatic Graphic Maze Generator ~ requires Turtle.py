import turtle
import random
import time

turtle.pencolor("White")
turtle.fillcolor("Red")
turtle.bgcolor("Black")
turtle.pensize(15)
turtle.shape("circle")
turtle.shapesize(0.5,0.5)
turtle.speed(50)
class Obj(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.directions = ["NORTH","EAST","SOUTH","WEST","N","E","S","W"]
        self.rooms = []
        
    def getX(self):
        return self.__x

    def increaseX(self, amount):
        self.__x += amount
        while turtle.heading() != 0:
            turtle.right(90)
        turtle.forward(amount*20)

    def getY(self):
        return self.__y

    def increaseY(self, amount):
        self.__y += amount
        while turtle.heading() != 90:
            turtle.left(90)
        turtle.forward(amount*20)

    def getRoom(self, x, y):
        for room in self.rooms:
            if x == room.getX() and y == room.getY():
                return room

class MazeGenerator(Obj):
    def __init__(self, x, y):
        super().__init__(x, y)
        while len(self.rooms) < 400: 
            x = self.getX()
            y = self.getY()
            roomExists = self.__roomExists(x, y) 
            directionExists = True
            possibleDirections = ["NORTH","EAST","SOUTH","WEST"] 
            if y == 19:
                possibleDirections.remove("NORTH")
            elif y == 0:
                possibleDirections.remove("SOUTH")
            if x == 19:
                possibleDirections.remove("EAST")
            elif x == 0:
                possibleDirections.remove("WEST")
            if roomExists:
                room = self.getRoom(x, y) 
                pathways = room.getPathways() 
                for directions in pathways: 
                    possibleDirections.remove(directions) 
            while directionExists: 
                if possibleDirections == []:
                    direction = self.__retrace() 
                    directionExists = False 
                else:
                    direction = possibleDirections[random.randint(0,len(possibleDirections)-1)] 
                    valid = self.__tryNextMove(x, y, direction) 
                    if valid: 
                        directionExists = True 
                        possibleDirections.remove(direction) 
                    else: 
                        directionExists = False 
            if not(roomExists): 
                newRoom = Room(x, y, direction) 
                self.rooms.append(newRoom) 
            else: 
                room.addPathways(direction) 
            if len(self.rooms) < 400:
                self.__move(direction) 

    def __retrace(self):
        x = self.getX()
        y = self.getY()
        possibleDirections = ["NORTH", "EAST", "SOUTH", "WEST"] 
        if y == 19:
            possibleDirections.remove("NORTH")
        elif y == 0:
            possibleDirections.remove("SOUTH")
        if x == 19:
            possibleDirections.remove("EAST")
        elif x == 0:
            possibleDirections.remove("WEST")
        exists = self.__roomExists(x, y) 
        if exists: 
            room = self.getRoom(x, y) 
            pathways = room.getPathways()
            for pathway in pathways: 
                possibleDirections.remove(pathway) 
        for direction in possibleDirections: 
            nextRoom = self.__getNextRoom(x, y, direction)
            nextRoomDirections = nextRoom.getPathways() 
            if direction == "NORTH" and "SOUTH" in nextRoomDirections:
                return direction
            elif direction == "EAST" and "WEST" in nextRoomDirections:
                return direction
            elif direction == "SOUTH" and "NORTH" in nextRoomDirections:
                return direction
            elif direction == "WEST" and "EAST" in nextRoomDirections:
                return direction
                
    def __getNextRoom(self, x, y, direction):
        complete = False
        while not(complete):
            for room in self.rooms: 
                roomX = room.getX()
                roomY = room.getY()
                if direction == "NORTH": 
                    if x == roomX and y+1 == roomY: 
                        nextRoom = room
                        complete = True
                elif direction == "EAST": 
                    if x+1 == roomX and y == roomY: 
                        nextRoom = room
                        complete = True
                elif direction == "SOUTH":
                    if x == roomX and y-1 == roomY:
                        nextRoom = room
                        complete = True
                elif direction == "WEST":
                    if x-1 == roomX and y == roomY:
                        nextRoom = room
                        complete = True
            return nextRoom #Return room
            
    def __tryNextMove(self, x, y, direction):
        if direction == "NORTH": 
            valid = self.__roomExists(x,y+1)
        elif direction == "EAST":
            valid = self.__roomExists(x+1,y)
        elif direction == "SOUTH":
            valid = self.__roomExists(x,y-1)
        elif direction == "WEST":
            valid = self.__roomExists(x-1,y)
        return valid

    def __move(self, direction):
        if direction == "NORTH": 
            self.increaseY(1) 
        elif direction == "EAST":
            self.increaseX(1)
        elif direction == "SOUTH":
            self.increaseY(-1)
        elif direction == "WEST":
            self.increaseX(-1)
            

    def __roomExists(self, x, y):
        for room in self.rooms: 
            roomX = room.getX()
            roomY = room.getY()
            if x == roomX and y == roomY:
                return True 
        return False 

class Room(Obj):
    def __init__(self, x, y, direction):
        super().__init__(x,y)
        self.__pathways = [direction]

    def addPathways(self, direction):
        self.__pathways.append(direction)

    def getPathways(self):
        return self.__pathways

while True:
    creator = MazeGenerator(9, 9)
    time.sleep(10)
    turtle.clear()
    turtle.pu()
    turtle.setx(0)
    turtle.sety(0)
    turtle.pd()
    input()
