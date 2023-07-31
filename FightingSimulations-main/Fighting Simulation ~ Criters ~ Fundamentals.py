import random, time

class Critter(object):
	def __init__(self, name, health, toHit, damage, defence):
		self.__name = name
		self.__health = health
		self.__toHit = toHit
		self.__damage = damage
		self.__defence = defence
		self.__alive = True
	
	def getName(self):return self.__name
	def getHealth(self):return self.__health
	def getToHit(self):return self.__toHit
	def getDamage(self):return self.__damage
	def getDefence(self):return self.__defence
	def isAlive(self):return self.__alive
	
	def reduceHealth(self,amount):
		self.__health -= amount
		if self.__health <= 0:
			self.__alive = False
			print("\tCritter {0} is dead!".format(self.__name))
	
	def attack(self,other):
		print("\n{0} attacks {1}.".format(self.getName(),other.getName()))
		roll = random.randint(0,9)
		if roll < self.getToHit():
			print("\t{0} hits!.".format(self.getName()))
			if other.defends():
				print("\t{0} defends!".format(other.getName()))
			else:
				damage = random.randint(1,self.getDamage())
				other.reduceHealth(damage)
				print("\tDeals {0} damage to {1}.".format(damage,other.getName()))
		else:
			print("\tMisses!")
			
	def defends(self):
		roll = random.randint(0,9)
		return roll <= self.__defence

class Spider(Critter):
	def __init__(self, name, health, toHit, damage, defence):
		super().__init__(name, health, toHit, damage, defence)
	
	def attack(self,other):
		for attack in range(8):
			super().attack(other)

class Elephant(Critter):
	def __init__(self, name, health, toHit, damage, defence):
		super().__init__(name, health, toHit, damage, defence)


class Crab(Critter):
	def __init__(self, name, health, toHit, damage, defence):
		#super().__init__() refers to the parent constructor
		super().__init__(name, health, toHit, damage, defence)

	def attack(self,other):
		for attack in range(2):
			super().attack(other)


class CritterFarm(object):

	def __init__(self):

		self.__spiders = 0
		self.__elephants = 0
		self.__crabs = 0
	
	def makeSpider(self):
		name = "Spider "+str(self.__spiders)
		self.__spiders += 1
		health = random.randint(5,9)
		toHit = 3
		damage = 2
		defence = 1
		return Spider(name,health,toHit,damage,defence)
	
	def makeElephant(self):
		name = "Elephant "+str(self.__elephants)
		self.__elephants += 1
		health = random.randint(12,18)
		toHit = 6
		damage = 7
		defence = 4
		return Elephant(name,health,toHit,damage,defence)

	def makeCrab(self):
		name = "Crab "+str(self.__crabs)
		self.__crabs += 1
		health = random.randint(3,6)
		toHit = 5
		damage = 3
		defence = 7
		return Crab(name,health,toHit,damage,defence)


class App(object):
	def __init__(self):
		self.__farm = CritterFarm() # aggregation!
		self.__critters = [] # critter list
	
	def main(self):
		num = int(input("How many critters? > "))
		for i in range(num):
			print("Critter number "+str(i + 1))
			print("Press")
			print("\t'C' for crab")
			print("\t'S' for spider")
			print("\t'E' for elephant")
			
			ok = False
			while not(ok):
				choice = input("> ")
				if choice.lower() in "cse":
					ok = True
			if choice.lower() == "c":
				self.__critters.append(self.__farm.makeCrab())
			elif choice.lower() == "e":
				self.__critters.append(self.__farm.makeElephant())
			elif choice.lower() == "s":
				self.__critters.append(self.__farm.makeSpider())
		print(self.__critters)

		gameOver = False
		while not(gameOver):
			for c in range(len(self.__critters)):
				if self.__critters[c].isAlive():
					ok = False
					while not(ok):
						t = random.randint(0,len(self.__critters)-1)
						if t != c and self.__critters[t].isAlive():
							ok = True
					self.__critters[c].attack(self.__critters[t])

					for i in range(3):
						print("\t\t\t.")
						time.sleep(0.1)

			newlist = []
			for i in self.__critters:
				if i.isAlive():
					newlist.append(i)
			self.__critters = []
			for i in newlist:
				self.__critters.append(i)

			if len(self.__critters) < 2:
				gameOver = True
		
		print("\n\nBattle is over!")
		print("\tRemaining critters: ")
		for i in self.__critters:
			print(i.getName())


critterFight = App()
critterFight.main()
