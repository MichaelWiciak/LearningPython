import random
import time

class Critter(object):
	
	def __init__(self,name,hp,chance_to_hit,mana):
		
		"""Creates critters with default values, randomly assigned with a certain interval.
		Also assigns every new variable into self.variable for easy access
		"""
		hp = random.randint(50,100)
		chance_to_hit = random.randint(10,100)
		self.name = str(name)
		self.hp = int(hp)
		self.chance_to_hit = chance_to_hit
		self.mana = 0
	
	def print_stats(self):
		""" It prints stats of the critter created"""
		print("Name:",self.name,"\tHP:",self.hp,"\tChance To Hit",self.chance_to_hit,"%\tMANA:", self.mana)
	
	def speak(self,name):
		
		print("Hi, I am ",self.name,"and my attacks do", self.attack)
	
	def victory_speech(self):
		""" Used the the critter wins a game to show who won"""
		print(self.name, "WON THE GAME!")
	
	def attack(self,other):
		"""The attack mechanism of the game, 1 attack at a random target per turn """
		
		chance = random.randint(0,100)
		if self.chance_to_hit >= chance:
			print(self.name, "hit", other.name,"for 5 damage")
			other.hp -= 5
			other.mana += 5
			self.mana += 10
		else:
			print(self.name, "missed and failed to hit", other.name)
	
	
	def dead_or_alive(self):
		if self.hp <= 0:
			return False###False == Dead
		else:
			return True
	
	def power(self):
		print("\t\t\t", self.name.upper(),"USES HEALING\n\t\t\t+20 HP")
		self.hp += 20

class CritterFarm(object):     
	
	def create(self, amount_of_critters_to_be_created):
		critter_list = []
		 
		for i in range(amount_of_critters_to_be_created):
			name = input("Name of Critter --->")
		
			print("What class do you want", name,"to be?\n==>1. Default\t ==>2. Tank\t ==>3. Assassin\t ==>4. AD Carry")
			choice = int(input('\t====>'))
			if choice == 1:
				critter_1 = Critter(name,0,0,0)
			elif choice == 2:
				critter_1 = Tank(name,0,0,0)
			elif choice == 3:
				critter_1 = Assassin(name,0,0,0)
			else:
				critter_1 = AD_Carry(name,0,0,0)
			
			critter_list.append(critter_1)
		self.main(critter_list)
	
	def main(self,critter_list):
		
		print("Who will win?")
		for y in range(len(critter_list)):
			critter_list[y].print_stats()		
		bet = input()	
		round_counter = 1
		while True:			
			alive_list = []
			input()	
			#time.sleep(5)
			print("---------------------------------------------------------------------------------------------------------")
			## Displays which round is it.
			print("Round",round_counter)
			round_counter += 1
			for i in range(len(critter_list)):
				if critter_list[i].dead_or_alive() == True:
					alive_list.append(critter_list[i])
				### THE BETTING SYSTEM
			if len(alive_list) == 1:
					alive_list[0].victory_speech()
					if bet.lower() == alive_list[0].name.lower():
						print("Your bet was correct!")
					else:
						print("Your bet was incorrect!")
			### Simulates the battle
			for i in range(len(alive_list)):
				length = len(alive_list)
				random_number  = random.randint(0,length-1)
				### No critter can attack itself
				while alive_list[i] == alive_list[random_number]:
					random_number  = random.randint(0,length-1)
				alive_list[i].attack(alive_list[random_number]) 
				 ##Checks every critter whether they are dead or 
				for x in range(len(alive_list)):
					if alive_list[x].dead_or_alive() == False: 
						print(alive_list[x].name, 'is dead and will be removed from the battle')
			
			for h in range(len(alive_list)):
				alive_list[h].print_stats() 
				if alive_list[h].mana >= 100:
					alive_list[h].mana -= 100
					print("\a\n\n\n\t\t\t", alive_list[h].name.upper(),"CASTS HIS SPECIAL ABILITY\n\n\n")							
					alive_list[h].power()
					
					### If only 1 critter is alive, end the game by giving a victory speech... Also, later, implement a automation of the game 
						### Also, at the end it leaves space without ending the program...
class App(object):
	
	def __init__(self):
		self._farm = CritterFarm()
		
	
	def sim1(self):
		amount_of_critters_to_be_created = int(input("How many critters do you want to create? ===>"))
		mycritters = self._farm.create(amount_of_critters_to_be_created)
		
class Tank(Critter):
	
	def __init__(self,name,hp,chance_to_hit,mana):
		super(Tank, self).__init__(name, hp, chance_to_hit,mana)
		self.hp = random.randint(80,150)
		self.chance_to_hit = random.randint(5,70) ###Overiding these stats
		
	def attack(self,other):
		chance = random.randint(0,100)
		if self.chance_to_hit >= chance:
			print(self.name, "hit", other.name,"for 3 damage")
			other.hp -= 3
			other.mana += 5
			self.mana += 10
		else:
			print(self.name, "missed and failed to hit", other.name)

class Assassin(Critter):
	
	def __init__(self,name,hp,chance_to_hit,mana):
		super(Assassin, self).__init__(name, hp, chance_to_hit,mana)
		self.hp = random.randint(30,70)
		self.chance_to_hit = random.randint(5,70) ###Overiding these stats
		
	def attack(self,other):
		chance = random.randint(0,100)
		if self.chance_to_hit >= chance:
			print(self.name, "hit", other.name,"for 11 damage")
			other.hp -= 11
			other.mana += 5
			self.mana += 10
		else:
			print(self.name, "missed and failed to hit", other.name)
	


class AD_Carry(Critter):
	
	def __init__(self,name,hp,chance_to_hit,mana):
		super(AD_Carry, self).__init__(name, hp, chance_to_hit,mana)
		self.hp = random.randint(20,60)
		self.chance_to_hit = random.randint(70,100) ###Overiding these stats
		
	def attack(self,other):
		chance = random.randint(0,100)
		if self.chance_to_hit >= chance:
			print(self.name, "hit", other.name,"for 6 damage")
			other.hp -= 6
			other.mana += 5
			self.mana += 10
		else:
			print(self.name, "missed and failed to hit", other.name)

	def power(self):
		print("\t\t\t", self.name.upper(),"USES PRECISION\n\t\t\t100% Chance to hit")
		self.chance_to_hit = 100


	
								
a = App()						
a.sim1()						

