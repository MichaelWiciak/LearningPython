import time, random

def quickSort(aList):
    lesser = []
    pivotList = []
    greater = []
    if len(aList) <= 1:
        return aList
    else:
        pivot = aList[0]
        for i in aList:
            if i < pivot:
                lesser.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                pivotList.append(i)
        lesser = quickSort(lesser)
        greater = quickSort(greater)
        return lesser + pivotList + greater
 

someList = []
for i in range(1000):
	someList.append(random.randint(1,100)+i)
print(someList)
start = time.time()
someList = quickSort(someList)
end = time.time()
print(end - start, 'seconds')
print(someList)



