class Array(object):
	def __init__(self, item):
		self.__array = []
		self.__size = 2
		self.__array.append(item)
		self.__array.append(None)
	
	def returnArray(self):		
		return self.__array
		
class ArrayException(Exception):
	def __init__(self, value):
		self.value = value
	def toString(self):
		return self.value


class LinkedList(object):
	
	def __init__(self):
		self.__mainList = []
		self.__tailPointer = 0
		self.__headPointer = 0

	def add(self, item):
		newArray = Array(item)
		theWholeArray = newArray.returnArray()
		self.__mainList.append(theWholeArray)
		self.__tailPointer += 1 
		if len(self.__mainList) > 1:	self.__mainList[self.__tailPointer-2][1] = self.__tailPointer - 1  
		else: self.__mainList[0][1] = None
		print(self.display()) ## Display this
		
	def display(self):
		return self.__mainList
	
	def pop(self):
		try:
			if not(len(self.__mainList) == 1):
				del(self.__mainList[self.__tailPointer-1])
				self.__tailPointer -= 1
				self.__mainList[self.__tailPointer-1][1] = None
				self.__mainList[self.__tailPointer-2][1] = self.__tailPointer-1
				if len(self.__mainList) == 1:
					self.__mainList[0][1] = None
			else: 
				del(self.__mainList[self.__tailPointer-1])
				self.__tailPointer -= 1
		except: raise ArrayException("List is Empty")		
		print(self.display())
		
	def shift(self, item): 
		if not(len(self.__mainList) == 0):			
			List = []
			List.append([None])
			for i in range(len(self.__mainList)):
				List.append(self.__mainList[i])
			List[0] = [item, 1]
			for i in range(len(self.__mainList)-1):
				List[i+1][1] += 1
			self.__mainList = List
			print(self.display())
		else:
			self.__mainList.append([item, None])
			print(self.display())
		self.__tailPointer += 1
			
	def unShift(self): # Remove from Front
		if self.__mainList:
			del(self.__mainList[self.__headPointer])
			for i in range(len(self.__mainList)-1):
				self.__mainList[i][1] -= 1
		else: raise ArrayException("The Array is empty")
		print(self.display())
		self.__tailPointer -= 1
	
	def getLength(self):
		return len(self.__mainList)
				
	def Remove(self, name):
		for i in range(len(self.__mainList)):
			if self.__mainList[i][0] == name:
				Place = i
				pass
		if not(self.__mainList[Place][1] == None):
			del(self.__mainList[Place])
			SmallerList = self.__mainList[Place-1:]
			BasePointer = self.__mainList[Place-1][1]
			for i in range(len(SmallerList)-2):
				SmallerList[i+1][1] = BasePointer + (i+1)
			self.__mainList[int(Place)-1:] = SmallerList
			print(self.display())
		else: 
			del(self.__mainList[Place])
			self.__mainList[Place-1][1] = None
			print(self.display())
		self.__tailPointer -= 1
		
	def Insert(self,Input, Position):
		List = self.__mainList
		List.insert(int(Position), [Input,0])
		SmallerList = List[int(Position)-1:]
		BasePointer = SmallerList[0][1] 
		for i in range(len(SmallerList)-2):
			SmallerList[i+1][1] = BasePointer + (i+1)
		self.__mainList[int(Position)-1:] = SmallerList
		self.__tailPointer += 1
		print(self.display())
	
	def peek(self,Place):
		try:
			return self.__mainList(Place)
		except:
			raise("Incorrect data type")


class App(object):
	
	def __init__(self):
		self.__linkedList = LinkedList()

	def main(self):
		try:
			Input = input("==>\t")
			if Input == '':
				self.__linkedList.pop()
			elif Input == "/":
				Input = input("Data >>>>\t")
				self.__linkedList.shift(Input)
			elif Input == '.':
				self.__linkedList.unShift()
			elif Input == '#':
				Input = input("Data >>>>>\t")
				self.__linkedList.Remove(Input)
			elif Input == ',':
				Input = input("Data >>>>>\t")
				Position = input("Position <<<<<\t")
				self.__linkedList.Insert(Input,Position)
			elif Input == '~':
				Position = input("Position >>>>>\t")
				self.__linkedList.peek(Position)
			elif Input == '$':
				print(self.__linkedList.getLength())
			elif Input:
				self.__linkedList.add(Input)
		except:
			print("Error...")
			
def start():
	print("""
ENTER 			--- Pop()
/     			--- Shift()
.      		        --- unShift()
#     			--- Remove()
,     			--- Insert()
~			--- Peek()
$			--- getLength()
any other input         --- Add()
	""")
	start = App()
	while True:
		try:
			start.main()
		except ArrayException:
			print("Invalid Input")

start()
	
