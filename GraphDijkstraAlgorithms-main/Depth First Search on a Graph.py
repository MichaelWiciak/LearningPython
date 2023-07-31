class mystack:
	def __init__(self, size):
		self.__stack = []
		self.__size = size
		for i in range (size):
			self.__stack.append("")
		self.__tos = -1

	def peek(self):
		if self.__isEmpty():
			pass
		else:
			return (self.__stack[ self.__tos ])
	
	def push(self, item):
		if not(self.__isFull()):
			self.__stack[ self.__tos + 1 ] = item
			self.__tos += 1
		else:
			print("STACK OVERFLOW")
			
	def pop(self):
		if not(self.__isEmpty()):
			self.__tos -= 1
			return self.__stack[self.__tos + 1]
		else:
			raise StackEmpty("Stack is empty")
			
	def __isEmpty(self):
		return (self.__tos == -1)

		
	def __isFull(self):
		return self.__tos == self.__size-1


	def display(self):
		for i in range (0, self.__tos+1 ):
			print (self.__stack[i], end=", ")


#There are many things wrong with this code, although it does work

class dfs(object):
	def __init__(self):
		#map is the adjacency list
		#visited keeps track of which nodes have been visited
		#stack is the stack of current nodes under investigation
		self.__map = {0:[1],
		1:[0,2,3],
		2:[1],
		3:[1,4,7],
		4:[5,6,9,3],
		5:[6,4],
		6:[11,4,5],
		7:[3,8],
		8:[9,20,7],
		9:[10,8,4],
		10:[11,22,9],
		11:[12,10,6],
		12:[13,11],
		13:[14,16,12],
		14:[15,13],
		15:[17,14],
		16:[18,13],
		17:[15,18],
		18:[17,25,23,16],
		19:[20],
		20:[8,21,19],
		21:[22,20],
		22:[10,23,21],
		23:[18,26,24,22],
		24:[23,26],
		25:[18],
		26:[23,27,24],
		27:[26]}
		self.__visited = []
		for i in range(len(self.__map.keys())):
			self.__visited.append(False)
		self.__stack = mystack(25)
	
	def main(self):
		start = 5
		
		current = start
		solved = False
		while not(solved):
			try:
				print("exploring node", current, end='-->')
				if not(self.__completed(current)):
					self.__stack.push(current)
				self.__visited[current] = True
				next = self.__findNextNode(current)
				if next != None:
					current = next
				else:
					current = self.__stack.pop()
					print("...dead-end...backtracking to", current, end='\n')
				self.__stack.display()
				#print()
				input()
					
			except StackEmpty as e:
				#assume maze is solved
				solved = True
				
		print("\nMaze fully explored by dfs :-)")
				
	
	def __findNextNode(self, p):
		nodes = self.__map[p]
		i = 0
		while i<len(nodes):
			if not(self.__visited[ nodes[i] ]):
				return self.__map[p][ i ]
			else:
				i += 1
		return None
	
	def __completed(self, p):
		nodes = self.__map[p]
		i = 0
		while i<len(nodes):
			if not(self.__visited[ nodes[i] ]):
				return False
			else:
				i += 1
		return True
		
					
			

class StackEmpty(Exception):
	def __init__(self, value):
		self.value = value
	def toString(self):
		return self.value 




app = dfs()
app.main()



