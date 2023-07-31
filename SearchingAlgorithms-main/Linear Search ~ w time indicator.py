import time, random

def linearSearch(alist, thing):
	p = 0
	found = False
	while not(found) and p < len(alist):
		if alist[p] == thing:
			found = True 
		else:
			p = p + 1 
	return found


someList = []
limit = 10000
target = 750
for i in range(limit):
	someList.append(random.randint(1,limit))
someList[limit-1] = target
print(someList)
start = time.time()
linearSearch(someList, target)
end = time.time()
print(end - start, 'seconds')






	
	
	
	
	
	
	
	
	
