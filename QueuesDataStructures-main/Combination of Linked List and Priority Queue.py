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
			
	def unShift(self): 
		if self.__mainList:
			item = self.__mainList[self.__headPointer][0][0]
			del(self.__mainList[self.__headPointer])
			for i in range(len(self.__mainList)-1):
				self.__mainList[i][1] -= 1
		else: raise ArrayException("The Array is empty")
		print(self.display())
		self.__tailPointer -= 1
		return item
	
	def getLength(self):
		return len(self.__mainList)
				
	def Remove(self, name):
		for i in range(len(self.__mainList)):
			if self.__mainList[i][0][0] == name:
				Place = i
				pass
		if not(self.__mainList[Place][1] == None):
			del(self.__mainList[Place])
			SmallerList = self.__mainList[Place-1:]
			BasePointer = self.__mainList[Place-1][1]
			for i in range(len(SmallerList)-2):
				SmallerList[i+1][1] = BasePointer + (i+1)
			self.__mainList[int(Place)-1:] = SmallerList
		else: 
			del(self.__mainList[Place])
			if not(Place == 0):
				self.__mainList[Place-1][1] = None
		self.__tailPointer -= 1
		
	def Insert(self,Input, Position):
		List = self.__mainList
		List.insert(int(Position), Input)
		Pointer = len(List)-1
		for i in range(len(List)-1):
			List[i][1] = Pointer-i 
		self.__mainList = List
		self.__tailPointer += 1
	
	def peek(self,Place):
		try: return self.__mainList(Place)
		except: raise("Incorrect data type")
	
	def ReturnPriority(self,NewPlace):
		return self.__mainList[NewPlace][0][1]
	
	def ReturnTheArray(self,NewPlace):
		return self.__mainList[NewPlace]
	
class PriorityQueue(object):
	
	def __init__(self):
		self.__linkedList = LinkedList()
		
	def addQueue(self,Input, Priority): 

		self.__linkedList.add([Input,Priority])
		NewPlace = self.__linkedList.getLength()
		if self.__linkedList.getLength() >= 2:
			for i in range(NewPlace-1):
				try:
					if self.__linkedList.ReturnPriority(NewPlace-1) == None:
						NewPlaceNewer = 0
					else:
						NewPlaceNewer = self.__linkedList.ReturnPriority(NewPlace-1)
						
					if int(NewPlaceNewer) < int(self.__linkedList.ReturnPriority(NewPlace-2)):

						theNewestArray = self.__linkedList.ReturnTheArray(NewPlace-1)
						theOlderArray = self.__linkedList.ReturnTheArray(NewPlace-2)
						self.__linkedList.Remove(theNewestArray[0][0])
						self.__linkedList.Remove(theOlderArray[0][0])
						self.__linkedList.Insert(theNewestArray, NewPlace-2)
						self.__linkedList.Insert(theOlderArray, NewPlace-1)
							
					NewPlace -= 1
				except:
					NewPlace -= 1
					continue
				
		print(self.__linkedList.display())
		
	def deQueue(self):
		try: 
			item = self.__linkedList.unShift()
			print("I have deQueued:", item)
		except:	raise ArrayException("The Array is empty")
				
class App(object):
	def __init__(self):		
		self.__priorityQueue = PriorityQueue()
	def main(self): 
		Input = input("Data --->\t")
		if Input:
			x = 'something random'
			while x:
				try: 
					Priority = int(input("Priority --->\t"))
					x = False
				except: print("Wrong data type...")
			self.__priorityQueue.addQueue(Input, Priority)
		else: 
			try: self.__priorityQueue.deQueue()
			except: print("The array is empty")
				
def start():
	start = App()
	while True: start.main()
	
start()
