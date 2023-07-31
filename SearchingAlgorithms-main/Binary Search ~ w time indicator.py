import time

def binarySearch( alist, item ):
	low = 0
	hi  = len(alist)
	finished = False
	while not finished:
		mid = (low + hi) // 2 # this is the important bit
		if item < alist[mid]:
			hi = mid
		else:
			low = mid
		if low == hi-1:
			finished = True
	if alist[mid] == item:
		return mid
	elif alist[mid-1]==item:
		return mid-1
	else:
		return -1

someList = []
limit = 1000000
target = 1
for i in range(limit):
	someList.append(i)
print(someList)
start = time.time()
index  = binarySearch(someList, target)
end = time.time()
if index != -1:
	print("Found it at position", index)
else:
	print("Cannot find it")
print(end - start, 'seconds')

