import math

class Array(object):
	def __init__(self, size):
		self.__size = size 
		self.array = []
		for i in range(size):
			self.array.append(0)

	def getSize(self):
		return self.__size

	def get(self, n):
		if n>= self.__size or n<0:
			raise ArrayException("Index "+str(n)+" out of bounds.")
		return self.array[n]

	def assign(self, n, value):
		if n>= self.__size or n<0:
			raise ArrayException("Index "+str(n)+" out of bounds.")
		self.array[n] = value
		

class ArrayException(Exception):
	def __init__(self, value):
		self.value = value
	def toString(self):
		return self.value 
		

def start():
	key_cat = "cat"
	key_dogs = "dogs"
	array = Array(10) 
	array.assign(5,"Cat") 
	array.assign(2,"Dogs") 
	hashFunction(key_cat)
	hashFunction(key_dogs)

def hashFunction(key):
    total = 0
    for i in key:
        num = ord(i)
        total += num
    total = total % 10
    k = 2**32 * abs(math.sin(total+1))
    print("Hash Table location for",key,":", k)

start()



