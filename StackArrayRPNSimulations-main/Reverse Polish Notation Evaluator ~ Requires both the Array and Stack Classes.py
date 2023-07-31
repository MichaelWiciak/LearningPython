class RPNcalc(object):
	def __init__(self):
		self.__stack = Stack(20) ## Change size according to needs
		self.__operators = ["*", "/", "+", "-" ]
		
	def main(self):
		while True:
			user = input("RPN Expression >>  ")
			parts = user.split()
			for i in parts:
				if i in self.__operators:
					try:
						x = self.__stack.pop()
						y = self.__stack.pop()
						answer = str(eval(y + i + x))
						self.__stack.push(answer)
					except Exception:
						print("Invalid Expression.")
				else:
					try:
						self.__stack.push(i)
					except:
						print("Expression is too long.")
			try:
				print("--> ",self.__stack.pop())
			except Exception:
				print("Empty Stack.")
		


























