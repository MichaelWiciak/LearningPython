import turtle as t
import math
import time

n=200  
d=360/n 
m=2     
r=300   

coord=[0,0]

t.bgcolor("Black")
t.color("White")
t.colormode(255)
t.ht()

def polToCart(r,theta,coord):                   
    coord[0]=r*math.cos(math.radians(theta))    
    coord[1]=r*math.sin(math.radians(theta))
    return coord   

def loopMult(n,d,m,r,multupto):
    for i in range(multupto):
        specific(n,d,r,i)
        time.sleep(1)
        t.clear()
    
def specific(n,d,r,s):
    t.tracer(0,0)            
    for i in range(n): 
        p=(s*i)%n          
        t.goto(polToCart(r,i*d,coord))
        t.pd()
        t.goto(polToCart(r,p*d,coord))  
        t.pu()
    t.update()

t.penup()                       
t.goto(polToCart(r,0,coord))   
t.pd()
loopMult(n,d,m,r,100)    