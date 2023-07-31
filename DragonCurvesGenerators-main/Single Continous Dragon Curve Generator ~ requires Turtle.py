import turtle
import time

length = 200
prevSeries = []

turtle.bgcolor("black")
turtle.speed(0)
turtle.ht()

while True:
        
    thickness = length/3
    length = length/(2**0.5)

    turtle.clear()
    turtle.color("#C75F08")
    turtle.pensize(thickness)
    turtle.forward(length)
    
    newSeries = []
    turnRight = True
    newSeries.append("R")
    
    for iteration in range(0,len(prevSeries)):
        newSeries.append(prevSeries[iteration])
        turnRight = not(turnRight)
        
        if turnRight:
            newSeries.append("R")
            
        else:
            newSeries.append("L")
            
        if prevSeries[iteration] == "R":
            turtle.right(90)
            turtle.color("#C86F18")
                
        elif prevSeries[iteration] == "L":
            turtle.left(90)
            turtle.color("#C75F08")
                
        turtle.forward(length)
        
    prevSeries = "".join(newSeries)
    prevSeries = list(prevSeries)
    time.sleep(3)

