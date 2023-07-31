def gameoflife(x_cycle):
    
    
    origin = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
              [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0], 
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1], 
              [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
        
    finalPopulation = copyTwoDimensionalList(origin)
    for x in range(x_cycle):
    
        testList = copyTwoDimensionalList(finalPopulation)
        rowNum = 0
        elementNum = 0
        
        for row in finalPopulation:
            elementNum = 0
            for element in row:
                if element == 1:
                    aListOfNeighbours = findNeighbour(finalPopulation, rowNum, elementNum)
                    testList[rowNum][elementNum] = decideWhatNext(aListOfNeighbours, True)
                   
                if element == 0:
                    aListOfNeighbours = findNeighbour(finalPopulation, rowNum, elementNum)
                    
                    testList[rowNum][elementNum] = decideWhatNext(aListOfNeighbours, False)
                    
                
                elementNum += 1
            
            rowNum +=1
        finalPopulation = copyTwoDimensionalList(testList)
        
    return finalPopulation
    
def findNeighbour(plain, row, column):
    
    aList= []
    #From top left anticlockwise to mid top
    try:
        i = row-1
        j = column-1
        if ifNegativeError(i) or ifNegativeError(j):
            raise IndexError
        aList.append(plain[i][j])
    except IndexError:
        aList.append(0)
    try:
        if ifNegativeError(column-1):
            raise IndexError
        aList.append(plain[row][column-1])
    except IndexError:
        aList.append(0)
    try:
        if ifNegativeError(column-1):
            raise IndexError
        aList.append(plain[row+1][column-1])
    except IndexError:
        aList.append(0)
    try:
        aList.append(plain[row+1][column])
    except IndexError:
        aList.append(0)
    try:
        aList.append(plain[row+1][column+1])
    except IndexError:
        aList.append(0)
    try:
        aList.append(plain[row][column+1])
    except IndexError:
        aList.append(0)
    try:
        if ifNegativeError(row-1):
            raise IndexError
        aList.append(plain[row-1][column+1])
    except IndexError:
        aList.append(0)
    try:
        if ifNegativeError(row-1):
            raise IndexError
        aList.append(plain[row-1][column])
    except IndexError:
        aList.append(0)

    
    return aList

def decideWhatNext(aListOfNeighbours, isItOne):
    
    if isItOne:
        
        numOfOnes = counter(aListOfNeighbours, 1)
        return decideIfOne(numOfOnes)
        
        
        
    else:
        numOfOnes = counter(aListOfNeighbours, 1)
        return decideIfZero(numOfOnes)
    
    
def counter(aList, value):
    counter = 0
    for i in aList:
        if i == value:
            counter += 1
            
    return counter


def copyTwoDimensionalList(aList):
    
    output = []
    
    for i in aList:
        aContainer = []
        for element in i:
            aContainer.append(element)
        output.append(aContainer)
    return output


def decideIfOne(numOnes):
    if numOnes == 2 or numOnes == 3:
        return 1
        
    elif numOnes < 2:
        return 0
        
    elif numOnes > 3:
        return 0
    
    
def decideIfZero(numOnes):
    if numOnes == 3:
        return 1
    return 0


def ifNegativeError(num):
    if num < 0:
        return True
