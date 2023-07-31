class Tree(object):
	def __init__(self):
		self.__struct = {}
		
		
	def add(self, item):
		p = 1
		b = "1"
		if len(self.__struct) == 0:
			self.__struct[1] = item
		else:
			found = False
			while not found:
				if item < self.__struct[p]:
					b += "0"
				else:
					b += "1"
				p = int(b,2)
				if not(p in self.__struct.keys()):
					self.__struct[p] = item
					found = True
		print(self.__struct)
		
		
	def search(self, item):
		if len(self.__struct) == 0:
			return False
		else:
			p = 1
			b = "1"
			found = False
			while not found:
				if item < self.__struct[p]:
					b += "0"
				else:
					b += "1"
				p = int(b,2)
				if not(p in self.__struct.keys()):
					return False
				if item == self.__struct[p]:
					found = True
			return True 

	def traverse(self):
		self.__traverse(1)
		
	def __traverse(self,a):
		p = int(bin(a)+"0",2)
		if p in self.__struct.keys():
			self.__traverse(p)
		print(self.__struct[a])
		#look right
		p = int(bin(a)+"1",2)
		if p in self.__struct.keys():
			self.__traverse(p)

		
