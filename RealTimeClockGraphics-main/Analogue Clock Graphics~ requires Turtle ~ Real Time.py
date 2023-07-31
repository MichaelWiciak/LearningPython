import turtle
import time

ok = False
while not(ok):
	offset = int(input("Enter offset from GMT (-11 to 11) :"))
	if offset >= -11 and offset <= 11:
		ok = True
		
wn = turtle.Screen()
wn.title("Analogue Clock")

SCALE = 1.7

mark = turtle.Turtle()
mark.speed(200)
mark.shape("circle")
for i in range(60):
      if i % 5 == 0:
            mark.pensize(10)
            mark.penup()
            mark.forward(200*SCALE)
            mark.pendown()
            mark.forward(10*SCALE)
            mark.penup()
            mark.backward(210*SCALE)
      else:
            mark.pensize(5)
            mark.penup()
            mark.forward(200*SCALE)
            mark.pendown()
            mark.forward(5*SCALE)
            mark.penup()
            mark.backward(205*SCALE)      
      mark.right(6)


update = True 
updateSecond = True
while True: 
      b = time.gmtime(time.time())
      m = b.tm_min 
      s = b.tm_sec 
      if update:
            hour = turtle.Turtle()
            hour.left(90)
            hour.speed(100*SCALE)
            hour.pensize(10)
            hour.shape("blank")
            hour.right(((b.tm_hour + offset) % 12) * 30 + b.tm_min * 0.5 )
            hour.backward(30*SCALE)
            hour.forward(160*SCALE)

            minute = turtle.Turtle()
            minute.speed(100)
            minute.shape("blank")
            minute.left(90)
            minute.pensize(6)
            minute.right((b.tm_min) * 6)
            minute.backward(30*SCALE)
            minute.forward(180*SCALE)

            update = False
            
      if updateSecond:
            second = turtle.Turtle()
            second.speed(100)
            second.shape("blank")
            second.color("red")
            second.left(90)
            second.pensize(3)
            second.right((b.tm_sec) * 6)
            second.backward(30*SCALE)
            second.forward(190*SCALE)
            updateSecond = False

      time.sleep(0.3)
      b = time.gmtime(time.time())
      new_min = b.tm_min
      new_sec = b.tm_sec

      if new_min != m:
            update = True
            hour.clear() 
            hour.reset()
            minute.clear()
            minute.reset()
      if new_sec != s:
            updateSecond = True
            second.clear()
            second.reset()
