class Maze(object):
	def __init__(self):
		self.__map = {0:[[1,1]],
		1:[[0,1],[2,1],[3,7]],
		2:[[1,1]],
		3:[[1,7],[4,4],[7,9]],
		4:[[5,1],[6,3],[9,15],[3,4]],
		5:[[6,1],[4,1]],
		6:[[11,27],[4,3],[5,1]],
		7:[[3,9],[8,6]],
		8:[[9,1],[20,2],[7,6]],
		9:[[10,1],[8,1],[4,15]],
		10:[[11,2],[22,1],[9,1]],
		11:[[12,12],[10,2],[6,27]],
		12:[[13,10],[11,12]],
		13:[[14,2],[16,2],[12,10]],
		14:[[15,3],[13,2]],
		15:[[17,30],[14,3]],
		16:[[18,2],[13,2]],
		17:[[15,30],[18,30]],
		18:[[17,30],[25,6],[23,5],[16,2]],
		19:[[20,5]],
		20:[[8,2],[21,1],[19,5]],
		21:[[22,1],[20,1]],
		22:[[10,1],[23,1],[21,1]],
		23:[[18,5],[26,5],[24,2],[22,1]],
		24:[[23,2],[26,2]],
		25:[[18,6]],
		26:[[23,5],[27,2],[24,2]],
		27:[[26,2]]}
	
	def getNode(self, n):
		return self.__map[n]

	def getLength(self):
		return len(self.__map.keys())
	
		
class ShortestPathFinder(object):
	def __init__(self, maze, show):
		self.__maze = maze
		self.showAll = show
	
	def main(self):
		l = self.__maze.getLength()
		s = int(input("Start point (0-"+str(l-1)+")"))
		e = int(input("End point (0-"+str(l-1)+")"))
		q = []
		for j in range(self.__maze.getLength()):
			q.append([999,None])	
		v = []
		c = s 
		q[c][0] = 0
		ok = False
		while not(ok):
			for i in self.__maze.getNode(c):
				if i[1]+q[c][0] < q[i[0]][0]:
					q[i[0]] = [i[1]+q[c][0],c]
			if self.showAll:
				print(q)
				input()
				print(v)
			v.append(c)
			c = self.__getNextNode(q,v)
			if c >-1:
				print("NEXT NODE IS ",c)
				print()
			else:
				print("The shortest path is")
				self.__shortestPathDisplayer(q,s,e)
				ok = True
				input()
				input()
				input()
			
	def __getNextNode(self,q,v):
		smallest = 999
		node = -1
		for i in range(len(q)):	
			if q[i][0] < smallest and i not in v:
				smallest = q[i][0] 
				node = i
		return node
	
	def __shortestPathDisplayer(self, q,s,e):
		c = e
		alist = []
		while c != s:
			alist.append(c)
			c = q[c][1]
		alist.append(s)
		alist.reverse()
		print(alist)	
		print("Distance ",q[e][0])
			
		
m = Maze()
user = input("Show working (Y/N)")
show = user.upper() in "YES"

a = ShortestPathFinder(m, show)
a.main()
