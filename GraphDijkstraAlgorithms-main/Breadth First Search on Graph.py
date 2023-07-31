class Node(object):
	def __init__(self, idnum, exitList):
		self.__id = idnum
		self.__entrance = None
		self.__exitList = exitList

	def __repr__(self):
		return "node "+str(self.__id)
		
	def getid(self):
		return self.__id
	
	def getExits(self):
		return self.__exitList

	def setEntrance(self, n):
		self.__entrance = n
	
	def getEntrance(self):
		return self.__entrance


class App(object):
	NUM_NODES = 28
	def __init__(self):
		self.__map = []
		self.__q = CircularQueue(App.NUM_NODES)
		self.__explicit = False
		
	def __createNodes(self):
		"""exits = [[1,5,4], [2,0], [3,1,6], [2], [0,8], [0,6,9,8], [2,7,9,5], [6], [4,5,9], [8,5,6]]"""
		exits = [[1],
		[0,2,3],
		[1],
		[1,4,7],
		[5,6,9,3],
		[6,4],
		[11,4,5],
		[3,8],
		[9,20,7],
		[10,8,4],
		[11,22,9],
		[12,10,6],
		[13,11],
		[14,16,12],
		[15,13],
		[17,14],
		[18,13],
		[15,18],
		[17,25,23,16],
		[20],
		[8,21,19],
		[22,20],
		[10,23,21],
		[18,26,24,22],
		[23,26],
		[18],
		[23,27,24],
		[26]]
		for i in range(App.NUM_NODES):
			n = Node( i, exits[i] )
			self.__map.append(n)
	
	def main(self):
		self.__createNodes()
		print("Shortest Path by Breadth First Search")
		start = int(input("START AT (0-27) : "))
		endPoint = int(input("END AT (0-27) : "))
		explicit = input("Show queue? (Y/N) :")
		if explicit.upper() in "YES":
			self.__explicit = True
		path = self.__findShortestPath(start, endPoint)
		print("\n\n(Press the 'any' key)")
		input()
		print("Shortest path from "+str(start)+" to "+str(endPoint))
		for i in path:
			print(i, end=', ')
	
	def __findShortestPath(self, start, endPoint):
        
		thepath = []
		Visited = set([])
		self.__q.enqueue(self.__map[start])
		complete = False
		while not complete:
			try:
				n = self.__q.dequeue()
				print("\nLooking at",n)
				Visited.add(n)
				i = 0 
				exitList = n.getExits()
				while not complete and i < len(exitList):
					exitNode = self.__map[exitList[i]] 				
					if exitNode.getEntrance() == None and start != exitNode.getid():
						print("  Exits to", exitNode, end=": ")
						print("connecting",exitNode,"to",n, end='')
						exitNode.setEntrance(n)
						if exitNode.getid() == endPoint:
							print(" Yay!\n\nFound route!")
							thepath = self.__reportPath(start, endPoint)
							complete = True
						else:
							print(" (queued",exitNode,")")
							if exitNode not in Visited:
								try:
									self.__q.enqueue(exitNode)
								except QueueError as e:
									print("That's an error",e)

					else:
						print("  Exits to", exitNode, end=": ")
						print("already connected to",exitNode.getEntrance())
					
					i += 1 
				if self.__explicit:
					print("|\n  Queued route")
					self.__q.display()
			except QueueError as e:
				print("That's an error",e)
		return thepath
		
	
	def __reportPath(self, start, endPoint):
		mylist = []
		finished = False
		n = self.__map[endPoint]
		mylist.append(n.getid())
		while not finished:
			n = n.getEntrance()
			mylist.append(n.getid())
			if n.getid() == start:
				finished = True
		mylist.reverse()
		return mylist


class CircularQueue(object):
	def __init__(self, size):
		self.__size = size
		self.__q = [None]*size
		self.__head = 0
		self.__tail = 0

	def __isBefore(self):
		return((self.__head - self.__tail == 1) or (self.__head == 0 and self.__tail == self.__size-1))

	def enqueue(self, item):
		if not(self.__isFull()):
			self.__q[self.__tail] = item
			self.__tail +=1
			if self.__tail == self.__size:
				self.__tail = 0
		else:
			raise QueueError("Queue is full")

	def dequeue(self):
		if not(self.__isEmpty()):
			item = self.__q[self.__head]
			self.__head += 1
			if self.__head == self.__size:
				self.__head = 0
			return(item)
		else:
			raise QueueError("Queue is empty")

	def peek(self):
		if not(self.__isEmpty()):
			return self.__q[self.__head]  
		else:
			raise QueueError("Queue is empty")
		
	def __isFull(self):
		return self.__isBefore()

	def __isEmpty(self):
		return self.__tail == self.__head

	def display(self):
		i = self.__head
		while (i != self.__tail):
			print("    ",self.__q[i])
			i += 1
			if i == self.__size:
				i = 0

class QueueError(Exception):
	def __init__(self, message):
		self.__message = message
	def toString(self):
		return "<Queue Error> "+self.__message




		
		
a = App()
a.main()			
