class LeapYearFinder(object):
    
    def __init__(self):
        pass
    
    def findLeapYear(self, startYear, endYear):
        
        leapYearRecord = []
        for i in range(int(startYear),int(endYear)):
            year = i
            print(year,end = "\t")
            #If year is divisible by 4 and not 100 unless it is also divisable by 400  
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):   
                print(year,  'is a leap year.')
                leapYearRecord.append(str(year))  
            else:
                print(year,  'is not leap year.')
        return leapYearRecord


    