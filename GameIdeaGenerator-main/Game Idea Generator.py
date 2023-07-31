import time, random

class GameIdeaGenerator(object):
    
    def __init__(self):
        
        self.__idea = [
        "fish","cat","dog","robot","school","amazing","unbelievable","incredible","magical","castle","maze","hunt","space","planet","ship","train","boat","plane","rocket","meteor","plant","elephant",
        "box","mathematical","cloudy","police","army","flower","tree","wizard","hand","bottle","banana","cheese","cake","chef","coffee","queen","princess","war","battle","chess","shop","basket",
        "waiter","man","human","alien","zombie","car","truck","road","paladine","adventure","alphabet","antediluvian","dinoasur","ASCII","astronaut","bitmap","blunderbuss","carnivorous","cleaner",
        "collector","dodge","evil","fairy","elf","gnome","farm","factory", "ghost","hospital","intragalactic","jump","laser","magnetic","manager","missile","music","ninja","noisy","number","omnipotent",
        "penguin","pixel","poet","poetic","prison","escape","quest","sauna","swamp","squirrel","soup","snakey","snake","toxic","poisonous","troll","trap","star","sun","moon","earth","werewolf","tower",
        "shaky","smelly","invisible","blue","red","green","pink","sneaky","windy","yeti","attack of the","revenge of the","return of the","zoo","media","spam","pirate","photo","booth","electrical","hummus",
        "pond","pondweed","merciless","determined","richochet","Trojan","probiscis","biodegradable","educational","mathematical","vampire","sheep","pig","cow","mole","digger","mine","bagpipe","misunderstood",
        "bee","nectar","voice","computer","doctor","skeleton","nippy","race","cinderella","cellar","teacher","thief","lawn","owl","prehistoric","futuristic","timetravelers","terrible","theory","library",
        "mysterious","ghoul","island","barbarian","travelling","mutants","slime","journey","radioactive","android","day of the","cyborg","viking","bandit","one-armed-bandit","temple","angry","indestructible",
        "trans-dimensional","brave","flying","critters","forest","unexpected","uninvited","legend","story","path","fast","detective","monsters","mission","crafty","silly","teenage","knight","dream","sleep",
        "walking","bullet-proof","underwater-flamethrower","hacker","programmer","dangerous","The last stand of","rescue the","find the","destroy the","carry the","make a"
        ]
        self.__setting = ["a school","your home","a garden","the park","a castle","a maze","space","a jungle","a war","prison","a forest","the beach","the moon","a lake","a factory","underwater","a restraunt",
        "a city","a workplace","an office","a motorway","a magical kingdom","a fishtank","inside your mind","a dream","a story","the future","the past"]
        self.__genre = ["shoot-em up","puzzle","roleplay","racing","platform","2D","text adventure","sandbox", "survival", "simulation"]
        self.__twist = ["you cannot touch the ground","only get one life","you are indestructible","enemies are invisible","you are stronger when it is the weekend","you must destroy an object",
        "it is multiplayer","you cannot do the same thing twice","everything is connected","its a race!","musical interlude","you must be good at maths","random spell test","it is in real time",
        "can only carry two objects at once","objects explode after ten seconds","you need to rescue someone","time limit changes when you whistle","there is random cheese everywhere",
        "some of the baddies actually like you, but which ones?","virtual reality","enemies can pass through walls","You can only touch something once","You need to touch everything twice",
        "there are levers","where are the monsters coming from?","everything is upside down","why is it dark in here?","Why would they do that?!","trust no-one","you can eat everything",
        "the floor is not stable","colours are important","what's that smell?","who is going to clean up after this?","mind what you say!","lasers!","patience is a virtue","you make the rules!",
        "slowest wins","smaller is better","bigger is better","there is more than one","timelimits","it is in French","you have to unlock the fire button","you only have one bullet",
        "monsters multiply","puzzles!","cat's like to sleep","walls everywhere","there are not enough ladders","exploding bananas!","there's always a bigger fish","everything is clockwork",
        "robots everywhere","everything could explode","don't move!","count everything twice!","be careful!"]
    
    def displayRandomIdea(self):
        input("Click anything button for an idea")
        print(">>>Thinking<<<")
        for i in range(3):
            time.sleep(1)
            print(".")
    	
        print("\n\nHow about a "+random.choice(self.__genre).upper()+" game\n")
        print('Which will somehow incorporate ',end='')
        repeat = 3
        for i in range(repeat):
            print(random.choice(self.__idea), end='')
            if i != repeat-1:
                print(', ', end='')
            else:
                print('.')
    	
        print("\nIt could take place in "+random.choice(self.__setting))
        print("\nMake it unique by following this rule:\t"+random.choice(self.__twist))
        input()
    
    
def test():
    a = GameIdeaGenerator()
    a.displayRandomIdea()

test()
    