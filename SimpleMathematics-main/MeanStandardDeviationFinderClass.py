import math

class MeanStandardDeviationFinder(object):
    
    def __init__(self):
        self.__records = []
        self.__numOfStudents = int(input("Enter number of students "))
        
    def dataEntry(self):
        for i in range(self.__numOfStudents):
            questionString = "Enter score for Student " + str(i+1)+' '
            score = int(input(questionString))
            self.__records.append(score)
            
    def findMeanStandardDeviation(self):
        total = sum(self.__records)
        mean = total / self.__numOfStudents
        squares = []
        for i in self.__records:
        	squares.append((mean-i)**2)
        variance = sum(squares)/self.__numOfStudents
        standard_dev = round(math.sqrt(variance),2)
        print("Mean is {0} and the s.d. is {1}".format(mean,standard_dev))
        return [mean,standard_dev]
    

        