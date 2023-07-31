import time, random

def bubbleSortOptimal( aList ):
	"""Performs the bubble sort on the list passed"""
	leaveLoop = False
	j = 0
	while not(leaveLoop):
		leaveLoop = True 
		for i in range(0, len(aList)-1 - j):
			if aList[i] > aList[i + 1]:
				aList[i], aList[i+1] = aList[i+1], aList[i]
				leaveLoop = False
		j = j + 1 

def bubbleSortNotOptimal( aList ):
	"""Performs the bubble sort on the list passed"""
	for j in range(len(aList)):
		for i in range(0, len(aList)-1):
			if aList[i] > aList[i + 1]:
				aList[i], aList[i+1] = aList[i+1], aList[i]


def bubbleSortLeaveLoopOnly( aList ):
	"""Performs the bubble sort on the list passed"""
	leaveLoop = False
	while not(leaveLoop):
		leaveLoop = True 
		for i in range(0, len(aList)-1):
			if aList[i] > aList[i + 1]:
				aList[i], aList[i+1] = aList[i+1], aList[i]
				leaveLoop = False


def bubbleSortUnsortedOnly( aList ):
	"""Performs the bubble sort on the list passed"""
	for j in range(len(aList)):
		for i in range(0, len(aList)-1-j):
			if aList[i] > aList[i + 1]:

				aList[i], aList[i+1] = aList[i+1], aList[i]


def merge_sort(m):
	if len(m) <= 1:
		return m
 
	middle = len(m) // 2
	left = m[:middle]
	right = m[middle:]
 
	left = merge_sort(left)
	right = merge_sort(right)
	return list(merge(left, right))

def merge(left, right):
	result = []
	left_idx, right_idx = 0, 0
	while left_idx < len(left) and right_idx < len(right):
		if left[left_idx] <= right[right_idx]:
			result.append(left[left_idx])
			left_idx += 1
		else:
			result.append(right[right_idx])
			right_idx += 1
	if left:
		result.extend(left[left_idx:])
	if right:
		result.extend(right[right_idx:])
	return result

TEST_SIZE = 4000

print("Setting up a random list")
a = []
b = []
c = []
d = []
e = []

for i in range(100):
	for j in range(40):
		a.append(i)
		b.append(i)
		c.append(i)
		d.append(i)
		e.append(i)

num = random.randint(10000,1000000)
a.insert(5,num)
b.insert(5,num)
c.insert(5,num)
d.insert(5,num)
e.insert(5,num)

print("OK - sorting")
print("\nNO OPTIMISATION")
start = time.time()
bubbleSortNotOptimal( a )
end = time.time()
print("sorted in {0} seconds".format(end - start))

input()

print("CHECK FOR NO SWAPS IN ONE PASS")
start = time.time()
bubbleSortLeaveLoopOnly( b )
end = time.time()
print("sorted in {0} seconds".format(end - start))

input()


print("SORT THE UNSORTED PART ONLY")
start = time.time()
bubbleSortUnsortedOnly( c )
end = time.time()
print("sorted in {0} seconds".format(end - start))

input()


print("OPTIMAL")
start = time.time()
bubbleSortOptimal( d )
end = time.time()
print("sorted in {0} seconds".format(end - start))


input()


print("MERGE SORT")
start = time.time()
merge_sort( d )
end = time.time()
print("sorted in {0} seconds".format(end - start))

