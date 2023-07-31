class NaiveQueue(object):
	def __init__(self, size):
		self._data = Array(size)
		self._size = size
		self._head = -1
		self._tail = 0
	
	def enQueue(self, item):
		#try to enqueue at the tail
		if self._tail < self._size:
			self._data.assign(self._tail, item)
			self._tail += 1
			if self._head == -1:
				self._head = 0
		else:
			raise QueueException("Cannot enqueue")
	
	def deQueue(self):
		#try to remove from the head
		if self._head >=0 and self._head < self._size:
			this = self._data.get(self._head)
			self._head += 1
			return this
		else:
			raise QueueException("Cannot dequeue")
	
	def display(self):
		print("-1\t\t",end='')
		if self._head == -1:
			print("HEAD")
		else:
			print(".")
		for i in range (self._size):
			if self._data.get(i) != None:
				print(str(i)+"\t"+self._data.get(i), end = '')
			else:
				print(str(i)+"\t  ", end = '')
			if i == self._head:
				print("\tHEAD")
			elif i == self._tail:
				print("\tTAIL")
			else:
				print("\t.")


class App(object):
	def __init__(self):
		self._Q = NaiveQueue(5)
	def main(self):
		while True:
			self._Q.display()
			item = input(">")
			if item == "":
				try:
					print("\nDequeued: "+self._Q.deQueue()+"\n")
				except QueueException as e:
					print(e.toString())
			else:
				try:
					self._Q.enQueue(item)
				except QueueException as e:
					print(e.toString())






class Array(object):
	def __init__(self, size):
		self.__size = size
		self.__array = []
		for i in range(size):
			self.__array.append(None)

	def getSize(self):
		return self.__size

	def get(self, n):
		if n>= self.__size or n<0:
			raise ArrayException("Index "+str(n)+" out of bounds.")
		return self.__array[n]

	def assign(self, n, value):
		if n>= self.__size or n<0:
			raise ArrayException("Index "+str(n)+" out of bounds.")
		self.__array[n] = value


class ArrayException(Exception):
	def __init__(self, value):
		self.value = value
	def toString(self):
		return self.value 

class QueueException(Exception):
	def __init__(self, value):
		self.value = value
	def toString(self):
		return self.value 


a = App()
a.main()

