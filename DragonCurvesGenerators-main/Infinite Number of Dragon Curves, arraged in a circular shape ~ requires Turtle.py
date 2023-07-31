import turtle
import time

counter = 0
y = 200
wn = turtle.Screen()
wn.bgcolor("black")
colour = 0
nameList = []
turtleList = []
list1 = []
iteration = 1
colour = 0
turtles = int(input("how many turtles:   "))

for i in range (0,turtles):
    nameList.append(str(i))

rotCount = 1
for a in nameList:
    print(a)
    a = turtle.Turtle()
    a.ht()
    a.pensize(y/3)
    turtleList.append(a)
    a.speed(0)
    if colour == 0:
        a.pencolor("#56c64f")
    if colour == 1:
        a.pencolor("#5ca358")
    if colour == 2:
        a.pencolor("#6a8968")
    if colour == 3:
        a.pencolor("#5ca358")
    if colour == 3:
        colour = -1

    a.right((360/turtles)*rotCount)
    colour = colour + 1
    rotCount = rotCount + 1
    a.forward(y)

rotation = 360/turtles
print(rotation)

print (turtleList)

def right(a):
    global colour
    a.right(90)
    a.forward(y)
    if colour == 0:
        a.pencolor("#56c64f")
    if colour == 1:
        a.pencolor("#5ca358")
    if colour == 2:
        a.pencolor("#6a8968")
    if colour == 3:
        a.pencolor("#5ca358")
    if colour == 3:
        colour = -1
    colour = colour + 1
    
def left(a):
    global colour
    a.left(90)
    a.forward(y)
    if colour == 0:
        a.pencolor("#56c64f")
    if colour == 1:
        a.pencolor("#5ca358")
    if colour == 2:
        a.pencolor("#6a8968")
    if colour == 3:
        a.pencolor("#5ca358")
    if colour == 3:
        colour = -1
    colour = colour + 1


while True:

    for a in turtleList:
          for i in list1:
                  if i == "r":
                    right(a)
                  if i == "l":
                    left(a)
          print (colour)
    list2 = ["r"]
    x = True
    
    for i in range(0,len(list1)):
        list2.append(list1[i])
        x = not(x)
        if x == True:
            list2.append("r")
        if x == False:
            list2.append("l")

    time.sleep(3)
    for a in turtleList:
        a.right(rotation)
        rotCount = rotCount + 1
        a.pensize(y/3)
        a.clear()

    iteration = iteration + 1
    list1 = list2
    y = (1/2*(((y**2)+(y**2))**(1/2)))
    counter = counter + 1


