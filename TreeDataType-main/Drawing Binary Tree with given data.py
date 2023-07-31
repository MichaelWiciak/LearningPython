import turtle

x = turtle.Turtle()
x.speed(100000)
x.penup()
x.setpos(0,200)
x.right(90)
x.write("Binary Tree",move=False, align="center", font=("Lucinda Console", 24, "normal"))
x.forward(60)
x.pendown()

class TestApp():
	def __init__(self):
		pass
		
	def main(self):
		data = [4,5,2,7,3,4,5,3,5,6,8,4, 1, 2, 3, 4, 5] ## change this for different data
		rootnode = Node(data[0],None)
		data.pop(0)
		for i in range(len(data)):
			rootnode.append(data[i])
		rootnode.display(0)
		rootnode.displaywithturtle(5)
		while True:
			x.forward(0.000000001)
			x.backward(0.000000001)


class Node(object):
	def __init__(self,data,parent):
		self.left = None
		self.right = None
		self.data = data
		self.parent = parent
		
	def append(self,data):
		if data <= self.data:
			self.leftappend(data)
		elif data > self.data:
			self.rightappend(data)
	def leftappend(self,data):
		if self.left == None:
			self.left = Node(data,self.data)
		else:
			self.left.append(data)
	def rightappend(self,data):
		if self.right == None:
			self.right = Node(data,self.data)
		else:
			self.right.append(data)
	
	def display(self,i):
		spaces = "\t" *i
		print(spaces,self.data)
		i+=1
		if self.left == None:
			print(spaces, "\tX")
		else:
			self.left.display(i)
		if self.right == None:
			print(spaces, "\tX")
		else:
			self.right.display(i)
	
	def displaywithturtle(self,i):
		x.write(self.data,move=False, align="center", font=("Lucinda Console", (150//i)+ 15, "normal"))
		x.forward(20)
		x.right(90)
		x.forward(800//i)
		x.left(90)
		x.forward(20)
		
		if self.left == None:
			x.backward(20)
			x.right(90)
			x.backward(800//i)
			x.left(90)
			x.backward(20)
		else:
			self.left.displaywithturtle(i*2)
			x.backward(20)
			x.right(90)
			x.backward(800//i)
			x.left(90)
			x.backward(20)
			
			
		x.forward(20)
		x.left(90)
		x.forward(800//i)
		x.right(90)
		x.forward(20)
		if self.right == None:
			x.backward(20)
			x.left(90)
			x.backward(800//i)
			x.right(90)
			x.backward(20)
		else:
			self.right.displaywithturtle(i*2)
			x.backward(20)
			x.left(90)
			x.backward(800//i)
			x.right(90)
			x.backward(20)
		
	


a = TestApp()
a.main()

