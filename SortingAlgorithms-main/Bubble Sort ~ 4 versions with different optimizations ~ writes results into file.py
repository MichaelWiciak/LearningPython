import time, random

def bubbleSortOptimal( aList ):
	"""Performs the bubble sort on the list passed
	Uses BOTH types of optimisation"""
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
	"""Performs the bubble sort on the list passed
	WITHOUT ANY optimisation"""
	for j in range(len(aList)):
		for i in range(0, len(aList)-1):
			if aList[i] > aList[i + 1]:
				aList[i], aList[i+1] = aList[i+1], aList[i]


def bubbleSortLeaveLoopOnly( aList ):
	"""Performs the bubble sort on the list passed
	Optimised by checking for a sorted list if 
	NO swaps are made in one pass"""
	leaveLoop = False
	while not(leaveLoop):
		for i in range(0, len(aList)-1):
			if aList[i] > aList[i + 1]:
				aList[i], aList[i+1] = aList[i+1], aList[i]
				leaveLoop = False


def bubbleSortUnsortedOnly( aList ):
	"""Performs the bubble sort on the list passed
	Only sorts the UNSORTED part of the list"""
	for j in range(len(aList)):
		for i in range(0, len(aList)-1-j):
			if aList[i] > aList[i + 1]:
				aList[i], aList[i+1] = aList[i+1], aList[i]


TEST_SIZE = 8000
FILE_NAME = "output.csv"


print("\nWorking...on "+FILE_NAME)
myfile = open(FILE_NAME,"w")
myfile.write("No optimisation,Look for no swaps,Sort unsorted only,Optimal\n")
for go in range(30):
	print(str(go))
	a = []
	b = []
	c = []
	d = []
	for i in range(TEST_SIZE):
		num = random.randint(0,100000)
		a.append(num)
		b.append(num)
		c.append(num)
		d.append(num)

	start = time.time()
	bubbleSortNotOptimal( a )
	end = time.time()
	ta = end-start

	start = time.time()
	bubbleSortLeaveLoopOnly( b )
	end = time.time()
	tb = end-start
	
	start = time.time()
	bubbleSortUnsortedOnly( c )
	end = time.time()
	tc = end-start
	
	start = time.time()
	bubbleSortOptimal( d )
	end= time.time()
	td = end-start
	
	myfile.write(str(ta)+","+str(tb)+","+str(tc)+","+str(td)+"\n")
myfile.close()
