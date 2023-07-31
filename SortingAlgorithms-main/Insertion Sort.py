def insertionSort(aList):
    first = 0
    last = len(aList)-1
    for CurrentPointer in range(first+1, last+1):
        CurrentValue = aList[CurrentPointer]
        Pointer = CurrentPointer - 1
        while aList[Pointer] > CurrentValue and Pointer >= 0:
            aList[Pointer+1] = aList[Pointer]
            Pointer -= 1
        aList[Pointer+1] = CurrentValue

