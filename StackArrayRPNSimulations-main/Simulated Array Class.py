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




